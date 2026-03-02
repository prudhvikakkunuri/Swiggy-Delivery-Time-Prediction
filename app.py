import streamlit as st
import pickle
import numpy as np

# Load model & features
with open("swiggy_delivery_time_rf.pkl", "rb") as f:
    model = pickle.load(f)

with open("final_features.pkl", "rb") as f:
    final_features = pickle.load(f)

st.set_page_config(page_title="Swiggy ETA Predictor", layout="centered")
st.title("🚴 Swiggy Delivery Time Prediction")
st.write("Enter order and rider details to predict delivery time (minutes).")

# Inputs (same order as final_features)
age = st.number_input("Delivery Person Age", min_value=18, max_value=60, value=28)
ratings = st.number_input("Ratings (1–5)", min_value=1.0, max_value=5.0, value=4.5, step=0.1)
vehicle_condition = st.selectbox("Vehicle Condition (0=Poor, 1=Average, 2=Good)", [0,1,2])
multiple_deliveries = st.selectbox("Multiple Deliveries (0 or 1)", [0,1])
distance = st.number_input("Distance (KM)", min_value=0.1, max_value=50.0, value=5.0)
traffic = st.selectbox("Traffic (Encoded: 0=low, 1=medium, 2=high, 3=jam)", [0,1,2,3])
festival_yes = st.selectbox("Festival? (1=Yes, 0=No)", [0,1])
order_time_hour = st.slider("Order Time Hour (0–23)", 0, 23, 12)
order_time_of_day_morning = st.selectbox("Morning? (1=Yes, 0=No)", [0,1])
weather_sunny = st.selectbox("Sunny? (1=Yes, 0=No)", [0,1])
city_type_urban = st.selectbox("Urban City? (1=Yes, 0=No)", [0,1])

if st.button("Predict ETA"):
    X = np.array([[age, ratings, vehicle_condition, multiple_deliveries, distance, traffic,
                   festival_yes, order_time_hour, order_time_of_day_morning,
                   weather_sunny, city_type_urban]])
    pred = model.predict(X)[0]
    st.success(f"⏱ Estimated Delivery Time: {round(pred, 2)} minutes")