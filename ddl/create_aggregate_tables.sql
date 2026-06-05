USE ecommerce_db.pem_curated;

CREATE TABLE IF NOT EXISTS aggregate_profit (
    year INT,
    category STRING,
    sub_category STRING,
    customer_name STRING,
    total_profit DECIMAL(18,2)
) USING DELTA;
