from pyspark.sql import functions as F
from transforms.api import Input, Output, transform_df


@transform_df(
    Output("ri.foundry.main.dataset.uani_events"),
    source=Input("ri.foundry.main.dataset.raw_uani_blog"),
)
def compute(source):
    return (
        source.withColumn("source", F.lit("UANI blog"))
        .withColumn("tags", F.array(F.lit("sanctions"), F.lit("iran"), F.lit("shipping")))
        .withColumn("severity", F.lit(3))
    )

