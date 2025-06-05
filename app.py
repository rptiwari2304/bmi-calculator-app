import streamlit as st

# Page setup
st.set_page_config(page_title="💪 Stylish BMI Calculator", layout="centered")

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        .title {
            color: #C71585;
            font-size: 32px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
        }
        .footer {
            font-size: 14px;
            text-align: center;
            color: #888;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">💖 Stylish BMI Calculator App</div>', unsafe_allow_html=True)
st.markdown("👤 **Owner**: Santosh Tiwari & Krishna Tiwari &nbsp;&nbsp;&nbsp;&nbsp; 👨‍💻 **Developer**: Ruchi")

# User Input
name = st.text_input("👩 Enter your name")
col1, col2 = st.columns(2)
with col1:
    height_cm = st.number_input("📏 Height (cm)", min_value=50.0, max_value=300.0, step=0.1)
with col2:
    weight_kg = st.number_input("⚖️ Weight (kg)", min_value=10.0, max_value=300.0, step=0.1)

if st.button("🧮 Calculate BMI"):
    if name and height_cm > 0 and weight_kg > 0:
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        st.markdown(f"### ✅ Hello **{name}**, Your BMI is: **{bmi:.2f}**")

        if bmi < 18.5:
            st.warning("📉 Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ Category: Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ Category: Overweight")
        else:
            st.error("🚨 Category: Obese")

        min_ideal_weight = 18.5 * (height_m ** 2)
        max_ideal_weight = 24.9 * (height_m ** 2)
        st.info(f"🎯 **Ideal Weight Range for your height:** {min_ideal_weight:.1f} kg – {max_ideal_weight:.1f} kg")
    else:
        st.error("❗ Please enter all details properly!")

# BMI Classification Table
with st.expander("📊 BMI Classification Table"):
    st.table({
        "BMI Range": ["< 18.5", "18.5 – 24.9", "25 – 29.9", "30 and above"],
        "Category": ["Underweight", "Normal", "Overweight", "Obese"]
    })

st.markdown('<div class="footer">👨‍💻 Developed by: ER Ruchi Tiwari</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
