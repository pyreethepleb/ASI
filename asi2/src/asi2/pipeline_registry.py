"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from asi2.pipelines import cars

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    #return {"data_processing": cars.create_pipeline()}
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
