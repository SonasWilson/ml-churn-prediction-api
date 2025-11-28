from fastapi import FastAPI
import joblib
import os
import pandas as pd
from api.schemas import InputData

app = FastAPI()

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

artifact = joblib.load(MODEL_PATH)
preprocessor = artifact["preprocessor"]
model = artifact["model"]

@app.get("/")
def home():
    return {"message": "API is running. Use /predict to get predictions."}

@app.post("/predict")
def predict(data: InputData):
    dict_data = data.model_dump()
    df = pd.DataFrame([dict_data])

    # Convert numeric fields to float
    numeric_cols = ["tenure", "MonthlyCharges", "TotalCharges"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.fillna(0)

    X_processed = preprocessor.transform(df)
    prediction = model.predict(X_processed)[0]

    return {"prediction": str(prediction)}
