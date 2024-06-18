from datetime import timedelta

from feast import FileSource, KafkaSource
from feast.data_format import JsonFormat, ParquetFormat

trans_stats_parquet_file = "../data_sources/HI-Small_trans_stats.parquet"

trans_stats_batch_source = FileSource(
    name="trans_stats",
    file_format=ParquetFormat(),
    path=trans_stats_parquet_file,
    timestamp_field="datetime",
    created_timestamp_column="created",
)

trans_stats_stream_source = KafkaSource(
    name="trans_stats_stream",
    kafka_bootstrap_servers="localhost:29092",
    topic="trans_stats",
    timestamp_field="datetime",
    batch_source=trans_stats_batch_source,
    message_format=JsonFormat(
        schema_json="Account string, Account.1 string, Timestamp string"
    ),
    watermark_delay_threshold=timedelta(minutes=5),
    description="The Kafka stream containing the trans stats",
)
