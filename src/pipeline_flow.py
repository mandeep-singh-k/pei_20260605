import os
from pyspark.sql import SparkSession
from src.data_ingestion import orders_df, products_df, customers_df
from src.aggregations import aggregate_table
from src.transformations import orders_enriched

spark = SparkSession.builder.appName("EcommercePipelineFlow").getOrCreate()

ddl_path = "ddl"
ddl_files = [
    "create_database.sql",
    "create_schema.sql",
    "create_orders_table.sql",
    "create_products_table.sql",
    "create_customers_table.sql",
    "create_enriched_tables.sql",
    "create_aggregate_tables.sql"
]

for ddl_file in ddl_files:
    file_path = os.path.join(ddl_path, ddl_file)
    with open(file_path, "r") as f:
        ddl_sql = f.read()
        spark.sql(ddl_sql)
        print(f"executed {ddl_file}")

#raw layer ignoring refined
orders_df.write.format("delta").mode("overwrite").saveAsTable("pem_raw.orders")
products_df.write.format("delta").mode("overwrite").saveAsTable("pem_raw.products")
customers_df.write.format("delta").mode("overwrite").saveAsTable("pem_raw.customers")
print("pei raw data ingested into pem_raw")

#curated layer
orders_enriched.write.format("delta").mode("overwrite").saveAsTable("pem_curated.enriched_orders")
print("pei enriched table populated")

aggregate_table.write.format("delta").mode("overwrite").saveAsTable("pem_curated.aggregate_profit")
print("pei aggregate table populated")
