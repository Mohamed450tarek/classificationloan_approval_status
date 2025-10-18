from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd

 
# -------------------------
model_uri = "runs:/3cb51c67f90c44d588d6bcbc50b717cd/xgb_model"  # ← غيّرها بالـ run_id الحقيقي
model = mlflow.pyfunc.load_model(model_uri)

 
app = FastAPI(title="Loan Approval API - MLflow Version")

 
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

 #route
# -------------------------
@app.post("/predict-mlflow")
def predict_loan(data: LoanData):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]
    result = "Approved" if prediction == 1 else "Rejected"
    return {"status": result}
