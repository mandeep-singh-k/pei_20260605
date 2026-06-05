import logging
from pyspark.sql import SparkSession

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

# ss Helper
def get_spark(app_name="EcommercePipeline"):
    return SparkSession.builder.appName(app_name).getOrCreate()

# sql execution Helper
def run_sql_file(spark, file_path):
    try:
        with open(file_path, "r") as f:
            sql_text = f.read()
        spark.sql(sql_text)
        logger.info(f"executed SQL file: {file_path}")
    except Exception as e:
        logger.error(f"failed to execute {file_path}: {e}")
        raise

# error handling Helper
def safe_write(df, table_name, mode="overwrite"):
    try:
        df.write.format("delta").mode(mode).saveAsTable(table_name)
        logger.info(f"data written to table: {table_name}")
    except Exception as e:
        logger.error(f"failed to write to {table_name}: {e}")
        raise
