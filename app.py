import streamlit as st
import pandas as pd
import joblib

# -------------------------------------------------
# Load trained pipeline
# -------------------------------------------------
model = joblib.load("readmission_model.pkl")

st.set_page_config(
    page_title="Diabetes Readmission Risk Predictor",
    layout="centered"
)

st.title("🏥 Diabetes Readmission Risk Predictor")
st.write(
    "This application estimates the risk of 30-day hospital readmission "
    "based on patient admission and utilization data."
)

st.markdown("---")

# -------------------------------------------------
# Input Form
# -------------------------------------------------
with st.form("patient_form"):
    age = st.selectbox(
        "Age Group",
        [
            "[0-10)", "[10-20)", "[20-30)", "[30-40)", "[40-50)",
            "[50-60)", "[60-70)", "[70-80)", "[80-90)", "[90-100)"
        ]
    )

    gender = st.selectbox("Gender", ["Male", "Female"])

    time_in_hospital = st.slider(
        "Time in Hospital (days)", 1, 14, 3
    )

    num_lab_procedures = st.slider(
        "Number of Lab Procedures", 1, 130, 40
    )

    num_medications = st.slider(
        "Number of Medications", 1, 50, 10
    )

    total_visits = st.slider(
        "Total Prior Hospital Visits", 0, 20, 1
    )

    submitted = st.form_submit_button("Predict Risk")

# -------------------------------------------------
# Prediction Logic
# -------------------------------------------------
if submitted:
    # Create full feature dictionary with safe defaults
    input_data = {col: 0 for col in model.feature_names_in_}

    # Override with user inputs
    input_data.update({
        "age": age,
        "gender": gender,
        "time_in_hospital": time_in_hospital,
        "num_lab_procedures": num_lab_procedures,
        "num_medications": num_medications,
        "total_visits": total_visits,
    })

    input_df = pd.DataFrame([input_data])

    # Predict probability
    risk_prob = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")
    st.metric("Readmission Risk Probability", f"{risk_prob:.2%}")

    # Threshold-based decision
    if risk_prob >= 0.35:
        st.error("⚠️ High Risk of 30-Day Readmission")
    else:
        st.success("✅ Low Risk of 30-Day Readmission")

    st.markdown(
        "_Note: Missing clinical inputs are assumed to be absent or zero, "
        "which reflects a conservative default for real-world deployment._"
    )