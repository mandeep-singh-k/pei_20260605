from pyspark.sql import SparkSession
from pyspark.sql.functions import year, sum as _sum, col

spark = SparkSession.builder.appName("EcommerceAggregations").getOrCreate()

orders_enriched = spark.table("pem_raw.enriched_orders")
aggregate_table = (
    orders_enriched
    .withColumn("year", year(col("order_date")))
    .groupBy("year", "category", "sub_category", "customer_name")
    .agg(_sum("profit").alias("total_profit"))
)

aggregate_table.write.format("delta").mode("overwrite").saveAsTable("pem_curated.aggregate_profit")
print("curated aggregate table created and populated in pem_curated schema")

# exposing df for pipeline_flow.py
__all__ = ["aggregate_table"]
