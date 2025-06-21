"""
This is a boilerplate pipeline 'cars'
generated using Kedro 0.19.13
"""
from autogluon.tabular import TabularPredictor, TabularDataset
import pandas as pd
from sklearn.model_selection import train_test_split



def load_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.head(10000)
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df.drop(["id", "url", "region", "region_url", "image_url", "VIN", "description", "county", "lat", "long", "posting_date"], axis=1, inplace=True)
    return df
def train_models(df: pd.DataFrame) -> TabularPredictor:
    predictor = TabularPredictor(label="price", path="models").fit(df, presets=["medium_quality","optimize_for_deployment"], time_limit=600,excluded_model_types=['RF', 'XT'])
    predictor.save("data/06_models/autogluon_models")
    return predictor
def predict_models(df: pd.DataFrame, predictor: TabularPredictor) -> pd.DataFrame:
    #predictor = TabularPredictor.load(predictor)
    example_data = {
        'year': 2004,
        'manufacturer': "ford",
        'model': "f-150",
        'condition': "good",
        'cylinders': "6 cylinders",
        'fuel': "gas",
        'odometer': 100000,
        'title_status': "clean",
        'transmission': "automatic",
        'drive': "4wd",
        'size': "full-size",
        'type': "truck",
        'paint_color': "red",
        'state': "tx"
    }
    example_df = pd.DataFrame([example_data])
    price = predictor.predict(example_df)
    print(price)
    print(predictor.predict(df))
    return predictor.predict(df)
# train test split
#train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)