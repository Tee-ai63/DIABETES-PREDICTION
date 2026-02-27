🏥 Diabetes Readmission Risk Prediction

📌 Project Overview

Hospital readmissions within 30 days are costly and often preventable.
This project builds a machine learning–based decision-support system to predict whether a patient with diabetes is at high risk of readmission within 30 days, using demographic, admission, utilization, and treatment-related data.

The goal is to prioritize recall to minimize missed high-risk patients, reflecting real-world clinical considerations.

🎯 Objective

Predict 30-day hospital readmission risk for diabetic patients

Optimize for recall to reduce false negatives

Provide an interpretable and deployable ML solution

📊 Dataset

Source: UCI Machine Learning Repository
Diabetes 130-US hospitals for years 1999–2008

Size: ~100,000 patient encounters

Data Type: Tabular healthcare data (de-identified)

The dataset includes patient demographics, hospital admission details, lab procedures, medication usage, and prior healthcare utilization.

🧾 Feature Summary

Key feature groups used:

Demographics: age group, gender, race

Hospital stay: admission type, source, discharge disposition, time in hospital

Utilization history: prior inpatient, outpatient, and emergency visits

Treatment indicators: medication changes, diabetes medication usage

Engineered features:

total_visits

high_utilizer

medication_count

binary readmission target (readmitted_binary)

High-cardinality diagnosis codes (e.g., ICD-9) were intentionally excluded to preserve interpretability and reduce sparsity.

🧹 Data Preparation

Missing values handled via imputation

Categorical variables encoded using one-hot encoding

Numerical variables scaled

All preprocessing handled inside a scikit-learn Pipeline to prevent data leakage

🧠 Modeling Approach
Baseline Model

Logistic Regression

Used to establish a performance baseline

Model Comparison

Logistic Regression

Random Forest

XGBoost

Models were evaluated using cross-validation, focusing on:

Recall

ROC-AUC

Final Model

XGBoost Classifier

Chosen due to:

Highest recall

Best ROC-AUC

Strong performance on imbalanced data

⚙️ Optimization & Evaluation

Stratified cross-validation

Hyperparameter tuning with GridSearchCV

Class imbalance handled via scale_pos_weight

Decision threshold calibrated to improve recall

Evaluation metrics:

Confusion matrix

ROC-AUC

Precision–Recall curve

🔍 Interpretability & Error Analysis

Feature importance analysis to understand key drivers of readmission

Error analysis focused on false negatives

Threshold calibration used to minimize missed high-risk patients

💼 Business & Clinical Perspective

False negatives are more costly than false positives in healthcare

Model prioritizes early identification of at-risk patients

Can support:

Care coordination

Discharge planning

Resource allocation

This model is intended as a decision-support tool, not a replacement for clinical judgment.

🌐 Deployment

Deployed using Streamlit

End-to-end pipeline (preprocessing + model) loaded via joblib

Handles missing inputs using conservative defaults

Outputs:

Readmission risk probability

Risk classification (High / Low)

⚠️ Limitations

Diagnosis codes not directly modeled

Retrospective observational data

Not validated on external hospital systems

🔮 Future Work

Group ICD diagnosis codes into clinical categories

Add SHAP-based explanations

Convert to API-based deployment (FastAPI)

Incorporate temporal modeling for patient history

📌 Key Takeaway

This project demonstrates an end-to-end applied machine learning workflow in healthcare — from data cleaning and modeling to evaluation, interpretation, and deployment — with a strong emphasis on clinical relevance and responsible ML practices.





