-- Task 4: execute against an empty DuckDB database.
-- First installation needs internet; LOAD spatial is required per connection.
INSTALL spatial FROM 'https://extensions.duckdb.org';
LOAD spatial;

CREATE TABLE operator (
    operator_id INTEGER PRIMARY KEY,
    operator_name VARCHAR NOT NULL UNIQUE
);

CREATE TABLE sa4_region (
    sa4_code VARCHAR PRIMARY KEY,
    sa4_name VARCHAR NOT NULL,
    state_name VARCHAR NOT NULL,
    boundary_year INTEGER NOT NULL CHECK (boundary_year = 2026),
    geom GEOMETRY -- EPSG:4326; NULL for ABS non-spatial regions.
);

-- A provider's station may be matched to several TfNSW records.
CREATE TABLE external_station (
    external_station_id VARCHAR PRIMARY KEY, -- e.g. ocm:272521 or osm:13428255938
    source VARCHAR NOT NULL CHECK (source IN ('ocm', 'osm')),
    source_station_id VARCHAR NOT NULL,
    station_name VARCHAR,
    operator_label VARCHAR, -- Source claim; not assumed equal to the cleaned operator.
    reported_bays INTEGER CHECK (reported_bays >= 0),
    max_power_kw DOUBLE CHECK (isfinite(max_power_kw) AND max_power_kw > 0),
    last_verified_utc TIMESTAMP, -- UTC, matching the provider verification timestamp.
    latitude DOUBLE NOT NULL CHECK (latitude BETWEEN -90 AND 90),
    longitude DOUBLE NOT NULL CHECK (longitude BETWEEN -180 AND 180),
    geom GEOMETRY NOT NULL, -- EPSG:4326, longitude first.
    UNIQUE (source, source_station_id),
    CHECK (external_station_id = source || ':' || source_station_id)
);

CREATE TABLE connector_type (
    connector_id INTEGER PRIMARY KEY,
    connector_name VARCHAR NOT NULL UNIQUE
);

CREATE TABLE external_station_connector (
    external_station_id VARCHAR REFERENCES external_station(external_station_id),
    connector_id INTEGER REFERENCES connector_type(connector_id),
    PRIMARY KEY (external_station_id, connector_id)
);

-- One price observation per external station in this snapshot, including missing prices.
CREATE TABLE station_pricing (
    external_station_id VARCHAR PRIMARY KEY REFERENCES external_station(external_station_id),
    raw_cost VARCHAR,
    amount DECIMAL(12, 6) CHECK (amount >= 0),
    currency VARCHAR CHECK (currency = 'AUD'),
    unit VARCHAR CHECK (unit IN ('kWh', 'minute', 'hour')),
    parse_status VARCHAR NOT NULL
        CHECK (parse_status IN ('unit_rate', 'free', 'fee_unpriced', 'unparsed', 'missing')),
    currency_assumed BOOLEAN NOT NULL,
    CHECK ((parse_status IN ('unit_rate', 'free')) = (amount IS NOT NULL)),
    CHECK ((currency IS NULL) = (unit IS NULL)),
    CHECK ((parse_status = 'unit_rate') = (currency IS NOT NULL)),
    CHECK (parse_status <> 'free' OR amount = 0),
    CHECK (NOT currency_assumed OR parse_status = 'unit_rate'),
    CHECK ((parse_status = 'missing') = (raw_cost IS NULL))
);

-- One retained source record, which can describe several plugs.
CREATE TABLE charger (
    charger_record_id VARCHAR PRIMARY KEY,
    station_name VARCHAR,
    station_address VARCHAR NOT NULL,
    operator_id INTEGER REFERENCES operator(operator_id),
    lga_name VARCHAR,
    postcode VARCHAR,
    source_program VARCHAR,
    charger_type VARCHAR NOT NULL CHECK (charger_type = 'DC'),
    number_of_plugs INTEGER CHECK (number_of_plugs > 0),
    rating_text VARCHAR,
    rating_kw DOUBLE CHECK (isfinite(rating_kw) AND rating_kw > 0),
    rating_representation VARCHAR NOT NULL,
    duplicate_status VARCHAR NOT NULL,
    latitude DOUBLE NOT NULL CHECK (latitude BETWEEN -90 AND 90),
    longitude DOUBLE NOT NULL CHECK (longitude BETWEEN -180 AND 180),
    geom GEOMETRY NOT NULL, -- EPSG:4326, longitude first.
    sa4_code VARCHAR REFERENCES sa4_region(sa4_code),
    sa4_match_count INTEGER NOT NULL CHECK (sa4_match_count >= 0),
    matched BOOLEAN NOT NULL,
    external_station_id VARCHAR REFERENCES external_station(external_station_id),
    match_method VARCHAR NOT NULL,
    match_distance_m DOUBLE CHECK (isfinite(match_distance_m) AND match_distance_m >= 0),
    match_is_ambiguous BOOLEAN NOT NULL,
    raw_record JSON NOT NULL, -- All original CSV fields, including quality flags.
    CHECK ((sa4_match_count = 1) = (sa4_code IS NOT NULL)),
    CHECK (matched = (external_station_id IS NOT NULL))
);

CREATE INDEX charger_geom_idx ON charger USING RTREE (geom);
CREATE INDEX sa4_geom_idx ON sa4_region USING RTREE (geom);

-- This view remains one row per charger; connectors use a separate view.
CREATE VIEW charger_analysis AS
SELECT c.*, o.operator_name, r.sa4_name, coalesce(e.source, 'none') AS match_source,
       e.operator_label AS external_operator, e.reported_bays AS external_bays,
       p.raw_cost, p.amount AS price_amount, p.currency AS price_currency,
       p.unit AS price_unit, p.parse_status AS price_status, p.currency_assumed
FROM charger c
LEFT JOIN operator o USING (operator_id)
LEFT JOIN sa4_region r USING (sa4_code)
LEFT JOIN external_station e USING (external_station_id)
LEFT JOIN station_pricing p USING (external_station_id);

CREATE VIEW charger_connector AS
SELECT c.charger_record_id, c.external_station_id, t.connector_id, t.connector_name
FROM charger c
JOIN external_station_connector ec USING (external_station_id)
JOIN connector_type t USING (connector_id);
