from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib
import pandas as pd
from data_load import load_data
from preprocess import preprocess_pipeline

def train_model():
    df = load_data("data/raw/telco_churn.csv")

    X = df.drop('Churn', axis='columns')
    y = df['Churn']

    preprocessor, num_cols, cat_cols = preprocess_pipeline(X)

    
    X_processed = preprocessor.fit_transform(X)

    
    X_train, X_test, y_train, y_test = train_test_split(
        X_processed, y, test_size=0.2, random_state=42
    )

    # Model
    model = RandomForestClassifier(n_estimators=200)
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {score}")

    # Saving only what API needs
    joblib.dump(
        {"preprocessor": preprocessor, "model": model},
        "api/model.pkl"
    )

if __name__ == "__main__":
    train_model()
