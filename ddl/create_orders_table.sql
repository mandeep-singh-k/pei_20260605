USE ecommerce_db.pem_raw;

CREATE TABLE IF NOT EXISTS orders (
    order_id STRING,
    customer_id STRING,
    product_id STRING,
    order_date DATE,
    quantity INT
) USING DELTA;
