from pyspark.sql import SparkSession
from pyspark.sql.functions import round, col

spark = SparkSession.builder.appName("EcommerceTransformations").getOrCreate()

orders_df = spark.table("pem_raw.orders")
products_df = spark.table("pem_raw.products")
customers_df = spark.table("pem_raw.customers")

orders_enriched = (
    orders_df
    .join(customers_df, "customer_id")
    .join(products_df, "product_id")
    .withColumn("profit", round(col("price_per_product"), 2))
    .select(
        "order_id",
        "customer_name",
        "country",
        "category",
        "sub_category",
        "profit",
        "order_date"
    )
)

orders_enriched.write.format("delta").mode("overwrite").saveAsTable("pem_curated.enriched_orders")

print("curated enriched table created and populated in pem_curated schema")

# exposing df for pipeline_flow.py
__all__ = ["orders_enriched"]
