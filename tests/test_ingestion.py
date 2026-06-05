import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder.appName("TestIngestion").getOrCreate()

def test_orders_table_exists(spark):
    df = spark.table("pem_raw.orders")
    assert df.count() > 0, "Orders table should not be empty"
    assert "order_id" in df.columns, "Orders table must have order_id column"

def test_products_table_exists(spark):
    df = spark.table("pem_raw.products")
    assert df.count() > 0, "products table should not be empty"
    assert "product_id" in df.columns, "Products table must have product_id column"

def test_customers_table_exists(spark):
    df = spark.table("pem_raw.customers")
    assert df.count() > 0, "Customers table should not be empty"
    assert "customer_id" in df.columns, "Customers table must have customer_id column"
