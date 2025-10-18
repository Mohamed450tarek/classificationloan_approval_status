#  Loan Approval Prediction System

##  Project Overview
This project is an end-to-end **Loan Approval Prediction System** built using **Machine Learning**, **MLflow**, and **FastAPI**.  
It predicts whether a loan application should be **approved or rejected** based on various applicant and financial attributes.

---

##  Dataset Description

The dataset contains the following main features:

| Feature | Description |
|----------|-------------|
| `no_of_dependents` | Number of dependents |
| `education` | Education level (`Graduate`, `Not Graduate`) |
| `self_employed` | Whether the applicant is self-employed (`Yes`, `No`) |
| `income_annum` | Applicant’s annual income |
| `loan_amount` | Loan amount requested |
| `loan_term` | Duration of the loan (in months) |
| `cibil_score` | Credit score |
| `residential_assets_value` | Value of residential assets |
| `commercial_assets_value` | Value of commercial assets |
| `luxury_assets_value` | Value of luxury assets |
| `bank_asset_value` | Total bank balance/assets |
| `loan_status` | Target label — `Approved` or `Rejected` |

---

## ⚙️ Steps Followed

### 1️⃣ Data Exploration & Preprocessing
- Handled missing values and categorical encoding in my data its be cleand nor have any missing values in it and data more cleand bit in project we in sure  from this in a begining in preprocessing .
- Normalized numerical features for better model performance.
- Split dataset into `train` and `test` sets (80/20).
- Used `ColumnTransformer` and `OneHotEncoder` for mixed-type preprocessing.
- Saved preprocessing pipeline using **joblib**.

### 2️⃣ Model Training & Evaluation
- Trained  one classification models:  
  - XGBoost  
  before that i used 2 classification model three give me  accuracy > 90% but i preeferd use  XGBoost ,
  becuse he give me most height performance 
- Tuned hyperparameters using GridSearchCV.  
- Selected the best model with **accuracy > 90%** .  
- Saved the trained model and preprocessor pipeline using **joblib**.

### 3️⃣ Experiment Tracking (MLflow)
- Used **MLflow** to track experiments, model parameters, and metrics.
- Each run logged:
  - Model type  
  - Accuracy,   
  - Serialized model artifacts  

### 4️⃣ Model Serving (FastAPI)
- Built a **FastAPI** app with two endpoints:
  - `/predict-joblib` → Uses locally saved joblib model
  - `/predict-mlflow` → Loads model directly from MLflow registry
- Used **Pydantic** models for input validation and schema enforcement.

### 5️⃣ Front-End (HTML)
- Created a simple one-page modern UI using HTML, CSS, and JS.
- Allows users to input loan application data and get real-time prediction results from the FastAPI backend.

### 6️⃣ Dockerization
- Containerized the app with **Docker** for easy deployment.
- Configured the container to expose the FastAPI API on port `8000`.

---

## 🚀 How to Run the Project Locally anouther way by using docker in line  103 --  line 133 most imprtant 

   - `/predict-joblib` → Uses locally saved joblib model in beging  you will run file **app_joblib.py**
after that run code to run local surver using  joilib **uvicorn app_joblib:app --reload**
 after that console output your local URL   **http://127.0.0.1:8**
can run in my page **Loan Approval.html** 
by inter localurl and API in any file as you need app_joilib.py  **http://127.0.0.1:8000/predict-joblib**
or 
from mlflow.tracking import MlflowClient
using mlflow RUN_ID
in cmd uvicorn app_mlflow:app --reload for running 

app_mlflow.py  **http://127.0.0.1:8000/predict-mlflow**
 if uou want inter data as backend for test on test program like postman 
 method POST 
 url  http://127.0.0.1:8000/predict-joblib , http://127.0.0.1:8000/predict-mlflow
 from body , raw  , example for json data that will you used it:
  {
  "no_of_dependents": 2,
  "education": "  Not graduated",
  "self_employed": " yes",
  "income_annum": 5400,
  "loan_amount": 128,
  "loan_term": 3400,
  "cibil_score": 750,
  "residential_assets_value": 200000,
  "commercial_assets_value": 50000,
  "luxury_assets_value": 30000,
  "bank_asset_value": 100000
}

and he give you result 
 
####  anouther way for deployment ############## using docker  ############
deploy and inference a machine learning model (built on the iris dataset) using Docker and FastAPI.

1. With terminal navigate to the root of this repository
--------------------------------------------------------

2. Build docker image
---------------------
.. code-block::

    docker build -t image_name .
   ##   ex : docker build -t loan-api .  ##

3. Run container

----------------
.. code-block::

    docker run --name container_name -p 8000:8000 image_name
 ##   ex : docker run -d -p 8000:8000 loan-api  ##

 all think must to be run on http://localhost:8000
 for api 
 ## http://localhost:8000/predict-joblib  ##
 

 ########## if  you want to sheck on koan applovel page on html ################
 change api in start page with 

 ## http://localhost:8000/predict-joblib ##
 
 
4. Output will contain
----------------------
INFO:     Uvicorn running on http://0.0.0.0:8000

http://localhost:8000/docs for check  on web 
 

### 🔧 1. Clone the Repository

