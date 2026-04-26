from pyspark.sql import functions as F
from transforms.api import Input, Output, transform_df


@transform_df(
    Output("ri.foundry.main.dataset.deepstatemap_events"),
    source=Input("ri.foundry.main.dataset.raw_deepstatemap_geojson"),
)
def compute(source):
    return (
        source.withColumn("source", F.lit("DeepStateMap mirror"))
        .withColumn("tags", F.array(F.lit("conflict"), F.lit("ukraine"), F.lit("map")))
        .withColumn("severity", F.lit(3))
    )

