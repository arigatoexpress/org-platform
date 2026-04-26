from pyspark.sql import functions as F
from transforms.api import Input, Output, transform_df


@transform_df(
    Output("ri.foundry.main.dataset.ofac_events"),
    source=Input("ri.foundry.main.dataset.raw_ofac_sdn"),
)
def compute(source):
    return (
        source.withColumn("source", F.lit("OFAC SDN"))
        .withColumn("tags", F.array(F.lit("sanctions"), F.lit("ofac")))
        .withColumn("severity", F.lit(4))
    )

