import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

st.title("🔐 ML-Based Website Protection System")

st.write("This system detects suspicious login behavior.")

# Input fields
login_attempts = st.number_input("Number of Login Attempts", min_value=0)
time_gap = st.number_input("Time Gap Between Attempts (seconds)", min_value=0)
request_count = st.number_input("Number of Requests Made", min_value=0)

if st.button("Check User"):

    user_data = np.array([[login_attempts, time_gap, request_count]])
    prediction = model.predict(user_data)

    if prediction[0] == 0:
        st.success("✅ Genuine User Detected")
        st.markdown("### Redirecting to Real Login Page...")
        st.markdown("[Click Here for Login](https://example.com)")
    else:
        st.error("⚠ Suspicious Activity Detected!")
        st.markdown("### Redirecting to Unknown Page...")
        st.markdown("[Unknown Page](https://example.org)")
