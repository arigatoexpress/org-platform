from transforms.api import Input, Output, transform_df


@transform_df(
    Output("ri.foundry.main.dataset.unified_events"),
    deepstate=Input("ri.foundry.main.dataset.deepstatemap_events"),
    ofac=Input("ri.foundry.main.dataset.ofac_events"),
    ais=Input("ri.foundry.main.dataset.ais_events"),
    uani=Input("ri.foundry.main.dataset.uani_events"),
)
def compute(deepstate, ofac, ais, uani):
    columns = ["id", "ts", "title", "source", "source_url", "severity", "tags", "mock"]
    return (
        deepstate.select(*columns)
        .unionByName(ofac.select(*columns), allowMissingColumns=True)
        .unionByName(ais.select(*columns), allowMissingColumns=True)
        .unionByName(uani.select(*columns), allowMissingColumns=True)
    )

