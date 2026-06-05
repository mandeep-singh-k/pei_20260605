from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, DateType
import urllib.request
import os

spark = SparkSession.builder.appName("EcommerceDataIngestion").getOrCreate()
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
        print(f"Executed {ddl_file}")

orders_schema = StructType([
    StructField("order_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("product_id", StringType(), True),
    StructField("order_date", DateType(), True),
    StructField("quantity", DoubleType(), True)
])

products_schema = StructType([
    StructField("product_id", StringType(), True),
    StructField("category", StringType(), True),
    StructField("sub_category", StringType(), True),
    StructField("product_name", StringType(), True),
    StructField("state", StringType(), True),
    StructField("price_per_product", DoubleType(), True)
])

customers_schema = StructType([
    StructField("customer_id", StringType(), True),
    StructField("customer_name", StringType(), True),
    StructField("email", StringType(), True),
    StructField("phone", StringType(), True),
    StructField("address", StringType(), True),
    StructField("segment", StringType(), True),
    StructField("country", StringType(), True),
    StructField("city", StringType(), True),
    StructField("state", StringType(), True),
    StructField("postal_code", StringType(), True),
    StructField("region", StringType(), True)
])

orders_url = "https://raw.githubusercontent.com/mandeep-singh-k/pei_20260605/main/data/Orders.json"
products_url = "https://raw.githubusercontent.com/mandeep-singh-k/pei_20260605/main/data/Products.csv"
customers_url = "https://raw.githubusercontent.com/mandeep-singh-k/pei_20260605/main/data/Customer.xlsx"

orders_df = spark.read.schema(orders_schema).json(orders_url)
products_df = spark.read.option("header", "true").schema(products_schema).csv(products_url)

local_customers_path = "/tmp/customers.xlsx"
urllib.request.urlretrieve(customers_url, local_customers_path)

customers_df = spark.read.format("com.crealytics.spark.excel") \
    .option("header", "true") \
    .schema(customers_schema) \
    .load(local_customers_path)

orders_df.write.format("delta").mode("overwrite").saveAsTable("pem_raw.orders")
products_df.write.format("delta").mode("overwrite").saveAsTable("pem_raw.products")
customers_df.write.format("delta").mode("overwrite").saveAsTable("pem_raw.customers")

print("pem raw tables created and populated in pem_raw schema")
