"""
This is a boilerplate pipeline 'cars'
generated using Kedro 0.19.13
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from asi2.pipelines.cars.nodes import load_data, clean_data, train_models, predict_models


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_data,
            inputs="vehicles",
            outputs="merged_data",
            name="load_data_node"
        ),
        node(
            func=clean_data,
            inputs="merged_data",
            outputs="cleaned_data",
            name="clean_datasets_node"
        ),
        node(
            func=train_models,
            inputs="cleaned_data",
            outputs="predictors",
            name="train_models_node"
        ),
        node(
            func=predict_models,
            inputs=["cleaned_data", "predictors"],
            outputs="result",
            name="predictions_node"
        )
])