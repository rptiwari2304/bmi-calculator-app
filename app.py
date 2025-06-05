import streamlit as st

# Page config
st.set_page_config(page_title="BMI Calculator", layout="centered")

# Title and developer name
st.title("💪 BMI (Body Mass Index) Calculator")
st.markdown("**Developed by: ER Ruchi Tiwari**")

# Sidebar for input
st.sidebar.header("📥 Enter Your Details")

# User input
name = st.sidebar.text_input("👤 Name")
height = st.sidebar.number_input("📏 Height (in cm)", min_value=50.0, max_value=250.0, step=1.0)
weight = st.sidebar.number_input("⚖️ Weight (in kg)", min_value=10.0, max_value=300.0, step=1.0)

# BMI Calculation
if st.sidebar.button("🧮 Calculate BMI"):
    if height > 0:
        height_m = height / 100  # convert to meters
        bmi = weight / (height_m ** 2)
        st.success(f"✅ {name}, your BMI is **{bmi:.2f}**")

        # BMI Category logic
        if bmi < 18.5:
            status = "Underweight"
            suggestion = "You should gain some weight to reach a healthy BMI."
        elif 18.5 <= bmi < 24.9:
            status = "Normal (Healthy)"
            suggestion = "Great! Keep maintaining your healthy lifestyle."
        elif 25 <= bmi < 29.9:
            status = "Overweight"
            suggestion = "Try to exercise and manage diet to reduce your BMI."
        else:
            status = "Obese"
            suggestion = "It is important to consult a doctor and work on a weight-loss plan."

        # Show result
        st.info(f"📊 You are classified as: **{status}**")
        st.write(f"💡 Suggestion: {suggestion}")

        # BMI Ranges Table
        st.markdown("### 📌 BMI Ranges:")
        st.markdown("""
        | BMI Range      | Category       |
        |----------------|----------------|
        | Below 18.5     | Underweight    |
        | 18.5 - 24.9    | Normal         |
        | 25 - 29.9      | Overweight     |
        | 30 and above   | Obese          |
        """)

    else:
        st.error("❌ Please enter a valid height!")
