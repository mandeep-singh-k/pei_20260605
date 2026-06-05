USE ecommerce_db.pem_raw;

CREATE TABLE IF NOT EXISTS customers (
    customer_id STRING,
    customer_name STRING,
    email STRING,
    phone STRING,
    address STRING,
    segment STRING,
    country STRING,
    city STRING,
    state STRING,
    postal_code STRING,
    region STRING
) USING DELTA;
