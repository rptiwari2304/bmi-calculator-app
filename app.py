import streamlit as st

# Page Setup
st.set_page_config(page_title="💪 BMI Calculator | Ruchi", layout="centered")

# Styling with CSS
st.markdown("""
    <style>
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        .title {
            background: linear-gradient(to right, #ff69b4, #ffa07a);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 36px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 1.5rem;
        }
        .footer {
            text-align: center;
            color: #555;
            font-size: 14px;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title"> Body Mass Index (BMI) Calculator</div>', unsafe_allow_html=True)

# User Inputs
name = st.text_input("📝 Your Name")
col1, col2 = st.columns(2)

with col1:
    height_cm = st.number_input("📏 Height in cm", min_value=50.0, max_value=250.0, step=0.1)
with col2:
    weight_kg = st.number_input("⚖️ Weight in kg", min_value=10.0, max_value=200.0, step=0.1)

if st.button("🔍 Calculate BMI"):
    if name and height_cm > 0 and weight_kg > 0:
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        st.markdown(f"### 👋 Hello **{name}**, your BMI is **{bmi:.2f}**")

        if bmi < 18.5:
            st.warning("🟡 Category: Underweight – You may need to gain weight.")
        elif 18.5 <= bmi < 24.9:
            st.success("🟢 Category: Normal – Keep maintaining your current health!")
        elif 25 <= bmi < 29.9:
            st.warning("🟠 Category: Overweight – Some lifestyle changes may help.")
        else:
            st.error("🔴 Category: Obese – Consider consulting a doctor.")

        min_ideal = 18.5 * (height_m ** 2)
        max_ideal = 24.9 * (height_m ** 2)
        st.info(f"💡 Ideal Weight Range: **{min_ideal:.1f} kg – {max_ideal:.1f} kg**")

    else:
        st.error("🚫 Please fill in all the fields properly.")

# Classification Table
with st.expander("📊 BMI Classification Table"):
    st.markdown("""
    | BMI Range      | Category       |
    |----------------|----------------|
    | Less than 18.5 | Underweight    |
    | 18.5 – 24.9    | Normal         |
    | 25 – 29.9      | Overweight     |
    | 30 and above   | Obese          |
    """)

# Footer
st.markdown('<div class="footer">💻 Developed by: ER Ruchi Tiwari</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
