import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def preprocess_pipeline(df: pd.DataFrame):

    # Clean numeric column 'TotalCharges'
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Fill missing numeric values
    numeric_cols = ["tenure", "MonthlyCharges", "TotalCharges"]
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    # Fill missing categorical values
    categorical_cols = df.columns.difference(numeric_cols)
    df[categorical_cols] = df[categorical_cols].fillna("Unknown")

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ],
        remainder="drop"
    )

    return preprocessor, numeric_cols, list(categorical_cols)
