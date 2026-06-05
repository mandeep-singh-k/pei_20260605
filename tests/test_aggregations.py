# import pytest
# from pyspark.sql import SparkSession

# @pytest.fixture(scope="module")
# def spark():
#     return SparkSession.builder.appName("TestAggregations").getOrCreate()

# def test_aggregate_profit_exists(spark):
#     df = spark.table("pem_curated.aggregate_profit")
#     assert df.count() > 0, "Aggregate profit table should not be empty"

# def test_aggregate_profit_columns(spark):
#     df = spark.table("pem_curated.aggregate_profit")
#     expected_columns = {
#         "year",
#         "category",
#         "sub_category",
#         "customer_name",
#         "total_profit"
#     }
#     assert expected_columns.issubset(set(df.columns)), \
#         f"Missing columns in aggregate_profit: {expected_columns - set(df.columns)}"

# def test_total_profit_calculation(spark):
#     df = spark.table("pem_curated.aggregate_profit")
#     sample = df.select("total_profit").filter(df.total_profit.isNotNull()).limit(1).collect()
#     assert len(sample) > 0, "total_profit column should have non-null values"
#     assert isinstance(sample[0]["total_profit"], (float, int)), "total_profit must be numeric"
