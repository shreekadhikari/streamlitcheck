import streamlit as st

st.title("BMI Calculator")

# User inputs
height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=250.0, value=170.0)
weight = st.number_input("Enter your weight (in kg):", min_value=10.0, max_value=200.0, value=70.0)

# BMI Calculation
if height and weight:
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.write(f"Your BMI is: **{bmi:.2f}**")

    # Classification
    if bmi < 18.5:
        st.warning("You're underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.info("You're overweight.")
    else:
        st.error("You're in the obese range.")
