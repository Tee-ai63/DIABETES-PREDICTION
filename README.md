# **🩺 Multi-Modal Diabetes Risk Prediction Using Machine Learning**
## **Project Overview**
- Diabetes is a chronic disease with severe long-term health and economic consequences if not detected early. This project develops a multi-modal machine learning system that predicts an individual’s risk of developing diabetes by combining tabular clinical data and longitudinal (time-series) patient data.

The system integrates traditional machine learning models with deep learning approaches to capture both static risk factors (e.g., age, BMI, glucose levels) and temporal health trends (e.g., rising blood glucose over time). Model predictions are made interpretable using explainable AI techniques to support clinical decision-making.

## **Objectives**
- Predict diabetes risk using patient clinical data
- Compare traditional ML models with advanced deep learning models
- Model disease progression using time-series data
- Handle missing and noisy medical data realistically
- Provide explainable predictions suitable for healthcare use

## **Methodology**
1. Data Sources
The project uses a combination of public medical datasets and synthetic patient history data to address privacy constraints and class imbalance.

2. Data Modalities
- Tabular Data
- Age, sex, BMI
- Blood glucose levels
- Blood pressure
- Insulin levels

Time-Series Data
- Sequential blood glucose measurements
- Longitudinal vitals over multiple visits

3. Data Preprocessing
- Missing value imputation (mean, median, forward-fill)
- Outlier handling and normalization
- Synthetic time-series generation for patient histories
- Train–test split with stratification

4. Models Implemented
Baseline Models

Logistic Regression

Random Forest

XGBoost

Advanced Models

Long Short-Term Memory (LSTM) network

Temporal Convolutional Neural Network (Temporal CNN)

Ensemble Strategy

Predictions from tabular and time-series models are combined to produce a unified diabetes risk score.

5. Model Evaluation

Accuracy

Precision, Recall, F1-score

ROC-AUC

Confusion Matrix

6. Model Explainability

SHAP (SHapley Additive exPlanations)

Feature importance visualization

Patient-level explanation of risk factors

📊 Dashboard (Optional Extension)

A Streamlit dashboard displays:

Individual diabetes risk score

Key contributing features

Risk progression over time

🛠️ Tech Stack

Python

Pandas, NumPy

Scikit-learn

XGBoost

TensorFlow / PyTorch

SHAP

Matplotlib, Seaborn

Streamlit