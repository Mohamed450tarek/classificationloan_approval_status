from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

 
# -------------------------
model = joblib.load("xgb_loan_model.pkl")
# ✅ Temporary fix for old XGBoost models
try:
    if hasattr(model, "use_label_encoder"):
        delattr(model, "use_label_encoder")
except Exception as e:
    print("⚠️ Skipping use_label_encoder fix:", e)

preprocessor = joblib.load("preprocessor.pkl")

 
# -------------------------
app = FastAPI(title="Loan Approval API - Joblib Version")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

 # data form 
# -------------------------
class LoanData(BaseModel):
    no_of_dependents: int
    education: str
    self_employed: str
    income_annum: float
    loan_amount: float
    loan_term: int
    cibil_score: float
    residential_assets_value: float
    commercial_assets_value: float
    luxury_assets_value: float
    bank_asset_value: float

 # route 
# -------------------------
@app.post("/predict-joblib")
def predict_loan(data: LoanData):
    input_data = [[
        data.no_of_dependents, data.education, data.self_employed,
        data.income_annum, data.loan_amount, data.loan_term, data.cibil_score,
        data.residential_assets_value, data.commercial_assets_value,
        data.luxury_assets_value, data.bank_asset_value
    ]]

    
    import pandas as pd
    columns = [
        'no_of_dependents', 'education', 'self_employed', 'income_annum',
        'loan_amount', 'loan_term', 'cibil_score', 'residential_assets_value',
        'commercial_assets_value', 'luxury_assets_value', 'bank_asset_value'
    ]
    df = pd.DataFrame(input_data, columns=columns)

    transformed = preprocessor.transform(df)
    prediction = model.predict(transformed)[0]
    
    result = "Approved" if prediction == 1 else "Rejected"
    return {"status": result}
