USE ecommerce_db.pem_curated;

CREATE TABLE IF NOT EXISTS enriched_orders (
    order_id STRING,
    customer_name STRING,
    country STRING,
    category STRING,
    sub_category STRING,
    profit DECIMAL(10,2),
    order_date DATE
) USING DELTA;
