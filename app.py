import streamlit as st

st.set_page_config(
    page_title="AI Fertilizer Recommendation System",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 AI Fertilizer Recommendation System")

st.write("""
Welcome to the AI Fertilizer Recommendation System.

This application will recommend the most suitable fertilizer
based on soil nutrients and environmental conditions.
""")

st.header("Enter Soil Details")

nitrogen = st.number_input("Nitrogen (N)", min_value=0)
phosphorus = st.number_input("Phosphorus (P)", min_value=0)
potassium = st.number_input("Potassium (K)", min_value=0)
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
moisture = st.number_input("Soil Moisture (%)")
ph = st.number_input("Soil pH")

if st.button("Recommend Fertilizer"):
    st.success("✅ Machine Learning prediction will be added in the next step.")
