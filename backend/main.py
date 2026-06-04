from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

app = FastAPI()

# Definim structura datelor de intrare (bazată pe Wisconsin Dataset)
# Pentru testare, folosim doar câteva câmpuri esențiale
class MedicalData(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    # Adaugă restul câmpurilor conform coloanelor din data.csv

# Încărcăm modelul antrenat anterior
try:
    with open('models/breast_cancer_xgboost.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None

@app.get("/")
def status():
    return {"message": "API Diagnostic Cancer Sân este activ"}

@app.post("/predict/tabular")
def predict_tabular(data: MedicalData):
    if model is None:
        raise HTTPException(status_code=500, detail="Modelul XGBoost nu a fost găsit.")
    
    # Transformăm datele primite într-un format acceptat de model (DataFrame)
    input_df = pd.DataFrame([data.dict()])
    
    # Realizăm predicția
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df).tolist()[0]
    
    result = "Malign" if prediction == 1 else "Benign"
    
    return {
        "prediction": result,
        "probability_malign": round(probability[1], 4),
        "probability_benign": round(probability[0], 4)
    }