import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "customerID" in df.columns:
        df = df.drop("customerID", axis='columns')
    return df