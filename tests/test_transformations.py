import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder.appName("TestTransformations").getOrCreate()

def test_enriched_orders_exists(spark):
    df = spark.table("pem_curated.enriched_orders")
    assert df.count() > 0, "Enriched orders table should not be empty"

def test_enriched_orders_columns(spark):
    df = spark.table("pem_curated.enriched_orders")
    expected_columns = {
        "order_id",
        "customer_name",
        "country",
        "category",
        "sub_category",
        "profit",
        "order_date"
    }
    assert expected_columns.issubset(set(df.columns)), \
        f"missing columns in enriched_orders: {expected_columns - set(df.columns)}"

def test_profit_calculation(spark):
    df = spark.table("pem_curated.enriched_orders")
    sample = df.select("profit").filter(df.profit.isNotNull()).limit(1).collect()
