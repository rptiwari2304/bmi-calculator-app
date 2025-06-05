import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (in kg):", min_value=1)
height = st.number_input("Enter your height (in cm):", min_value=1)

if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.write(f"Your BMI is: **{bmi:.2f}**")
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.info("You are overweight.")
    else:
        st.error("You are obese.")
