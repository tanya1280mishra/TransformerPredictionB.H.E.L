import streamlit as st
import pandas as pd
import joblib

# Load models
classifier_model = joblib.load('classifier_model.pkl')
regression_model = joblib.load('regression_model.pkl')

# Define feature columns
feature_columns = [
    'H2_mean', 'H2_std', 'CO_mean', 'CO_std',
    'C2H4_mean', 'C2H4_std', 'C2H2_mean', 'C2H2_std'
]

# Sidebar inputs
st.sidebar.header("Input Gas Features")
input_data = {}
for col in feature_columns:
    input_data[col] = st.sidebar.number_input(f"{col}", step=0.0001)

# Convert input to DataFrame
input_df = pd.DataFrame([input_data])

# Predict
if st.button("Predict"):
    class_pred = classifier_model.predict(input_df)[0]
    reg_pred = regression_model.predict(input_df)[0]

    # Class mapping
    class_map = {
        1: "Normal class",
        2: "Partial Discharge",
        3: "Low Energy Discharge",
        4: "Low-Temperature Overheating"
    }

    class_label = class_map.get(class_pred, "Unknown Class")

    # Show results
    st.subheader("🧠 Classification Result")
    st.write(f"Predicted Class Code: {class_pred}")
    st.success(f"Class Description: {class_label}")

    st.subheader("📈 Regression Result")
    st.write(f"Predicted Remaining Useful Life (RUL): {reg_pred:.2f}")
