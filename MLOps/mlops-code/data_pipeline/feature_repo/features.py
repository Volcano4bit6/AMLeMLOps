from datetime import timedelta

from feast import FeatureView, Field
from feast.stream_feature_view import stream_feature_view
from feast.types import Float64, Int64, String
from pyspark.sql import DataFrame

from data_sources import trans_stats_batch_source, trans_stats_stream_source
from entities import account

trans_stats_view = FeatureView(
    name="trans_stats",
    description="trans features",
    entities=[account],
    ttl=timedelta(days=36500),
    schema=[
        Field(name="From Bank", dtype=Int64),
        Field(name="To Bank", dtype=Int64),
        Field(name="Account.1", dtype=String),
        Field(name="Amount Received", dtype=Float64),
        Field(name="Receiving Currency", dtype=String),
        Field(name="Amount Paid", dtype=Float64),
        Field(name="Payment Currency", dtype=String),
        Field(name="Payment Format", dtype=String),
        Field(name="Is Laundering", dtype=Int64)
    ],
    online=True,
    source=trans_stats_batch_source,
    tags={},
    owner="sontvh2002@gmail.com",
)


@stream_feature_view(
    entities=[account],
    ttl=timedelta(days=36500),
    mode="spark",
    schema=[
        Field(name="From Bank", dtype=Int64),
        Field(name="To Bank", dtype=Int64),
        Field(name="Account.1", dtype=String),
        Field(name="Amount Received", dtype=Float64),
        Field(name="Receiving Currency", dtype=String),
        Field(name="Amount Paid", dtype=Float64),
        Field(name="Payment Currency", dtype=String),
        Field(name="Payment Format", dtype=String),
        Field(name="Is Laundering", dtype=Int64)
    ],
    timestamp_field="datetime",
    online=True,
    source=trans_stats_stream_source,
    tags={},
    owner="stream_source_owner@gmail.com",
)
def trans_stats_stream(df: DataFrame):
    from pyspark.sql.functions import col

    return (df)
    # return (
    #     df.withColumn("conv_percentage", col("conv_rate") * 100.0)
    #     .withColumn("acc_percentage", col("acc_rate") * 100.0)
    #     .drop("conv_rate", "acc_rate")
    #     .withColumnRenamed("conv_percentage", "conv_rate")
    #     .withColumnRenamed("acc_percentage", "acc_rate")
    # )
