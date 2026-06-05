USE ecommerce_db.pem_raw;

CREATE TABLE IF NOT EXISTS products (
    product_id STRING,
    category STRING,
    sub_category STRING,
    product_name STRING,
    state STRING,
    price_per_product DOUBLE
) USING DELTA;
