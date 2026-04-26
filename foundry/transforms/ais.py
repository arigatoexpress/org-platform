from pyspark.sql import functions as F
from transforms.api import Input, Output, transform_df


@transform_df(
    Output("ri.foundry.main.dataset.ais_events"),
    source=Input("ri.foundry.main.dataset.raw_aisstream"),
)
def compute(source):
    return (
        source.withColumn("source", F.lit("AISStream"))
        .withColumn("tags", F.array(F.lit("ais"), F.lit("maritime"), F.lit("shipping")))
        .withColumn("severity", F.lit(2))
    )

