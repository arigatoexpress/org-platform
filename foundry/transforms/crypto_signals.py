from pyspark.sql import functions as F
from transforms.api import Input, Output, transform_df


@transform_df(
    Output("ri.foundry.main.dataset.market_signals"),
    source=Input("ri.foundry.main.dataset.raw_crypto_watchlist"),
)
def compute(source):
    return source.withColumn("source", F.lit("org-platform crypto score")).withColumn(
        "signal_type", F.lit("token_watchlist")
    )

