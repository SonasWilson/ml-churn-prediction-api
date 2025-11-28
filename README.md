
````markdown
# Churn Prediction API

**End-to-End ML Project: Predict Customer Churn Using Python, Scikit-learn, FastAPI, and Docker**

---

## Project Overview

This project demonstrates a complete machine learning workflow to predict customer churn for a telecom company. The pipeline includes:

- Data loading and preprocessing  
- Training a Random Forest classifier  
- Building a REST API with FastAPI for real-time predictions  
- Containerizing the application using Docker for easy deployment  

---

## Tech Stack

- **Programming:** Python 3.12  
- **ML Libraries:** Scikit-learn, Pandas, NumPy, Joblib  
- **API Framework:** FastAPI  
- **Containerization:** Docker  
- **Version Control:** Git & GitHub  

---

## Features

- End-to-end ML pipeline: from raw data to predictions  
- FastAPI endpoint `/predict` for sending JSON data and receiving churn prediction  
- Preprocessing integrated with model inference  
- Dockerized application for reproducible deployment  
- Sample input data provided in `InputData` Pydantic model  

---

## Model Performance

- **Model:** Random Forest Classifier  
- **Accuracy on Test Data:** X%  *(replace X with your actual score)*  

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/SonasWilson/ml-churn-prediction-api.git
cd ml-churn-prediction-api
````

### 2. Run Locally with Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
python src/train.py        # Train the model
uvicorn api.main:app --reload
```

Access the API at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 3. Run Using Docker

```bash
docker build -t churn-api .
docker run -p 8000:8000 churn-api
```

Access the API in your browser: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Example Request

POST to `/predict` with JSON body:

```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "DSL",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 50.2,
  "TotalCharges": 602.4
}
```

Response:

```json
{
  "prediction": "Yes"
}
```

---

## Links

* **GitHub Repository:** [https://github.com/SonasWilson/ml-churn-prediction-api](https://github.com/SonasWilson/ml-churn-prediction-api)
* **Docker Hub Image:** [https://hub.docker.com/r/sonawilson/churn-api](https://hub.docker.com/r/sonawilson/churn-api)

---

## Author

* Your Name
* LinkedIn: [https://www.linkedin.com/in/sonapwilson/](https://www.linkedin.com/in/sonapwilson/)
* GitHub: [https://github.com/SonasWilson](https://github.com/SonasWilson)

---

## License

This project is open source and available under the MIT License.

```



