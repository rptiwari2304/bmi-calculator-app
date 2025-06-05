import streamlit as st

st.set_page_config(page_title="BMI Calculator App", layout="centered")

st.title("💪 BMI Calculator App")
st.markdown("👨‍💻 Developed by **Ruchi**")

st.markdown("## 🔢 Enter Your Name")

# Input from user
height_cm = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=300.0, step=0.1)
weight_kg = st.number_input("Enter your weight (in kg):", min_value=10.0, max_value=300.0, step=0.1)

if st.button("Calculate BMI"):
    if height_cm > 0 and weight_kg > 0:
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        st.success(f"✅ Your BMI is: **{bmi:.2f}**")

        # BMI Categories
        if bmi < 18.5:
            st.warning("📉 Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ Category: Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ Category: Overweight")
        else:
            st.error("🚨 Category: Obese")

        # Ideal weight calculation based on BMI 18.5 to 24.9
        min_ideal_weight = 18.5 * (height_m ** 2)
        max_ideal_weight = 24.9 * (height_m ** 2)

        st.markdown(f"🎯 **Ideal Weight Range:** {min_ideal_weight:.1f} kg to {max_ideal_weight:.1f} kg")

    else:
        st.error("❌ Please enter valid height and weight!")

# BMI Info Table
st.markdown("## 📊 BMI Classification Table")
st.table({
    "BMI Range": ["< 18.5", "18.5 – 24.9", "25 – 29.9", "30 and above"],
    "Category": ["Underweight", "Normal", "Overweight", "Obese"]
})
