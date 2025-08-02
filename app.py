import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Streamlit page settings
st.set_page_config(page_title="Flight Price Predictor", layout="centered")

# Title and description
st.title("✈️ Flight Ticket Price Predictor")
st.markdown("Enter flight details to predict the ticket price 💸")

# User input fields
airline = st.selectbox("Airline", ["Jet Airways", "IndiGo", "Air India", "SpiceJet", "Vistara"])
source = st.selectbox("Source", ["Delhi", "Kolkata", "Mumbai", "Chennai", "Bangalore"])
destination = st.selectbox("Destination", ["Cochin", "Delhi", "New Delhi", "Hyderabad", "Kolkata", "Bangalore"])
total_stops = st.selectbox("Total Stops", ["non-stop", "1 stop", "2 stops", "3 stops", "4 stops"])
journey_day = st.slider("Journey Day", 1, 31, 1)
journey_month = st.slider("Journey Month", 1, 12, 1)
duration_mins = st.number_input("Duration (in minutes)", min_value=30)
dep_hour = st.slider("Departure Hour", 0, 23, 10)
dep_min = st.slider("Departure Minute", 0, 59, 0)

# Preprocess input
def preprocess_input():
    # Encode categorical variables manually (must match training encoding!)
    airline_dict = {
        "Jet Airways": 0, "IndiGo": 1, "Air India": 2,
        "SpiceJet": 3, "Vistara": 4
    }
    source_dict = {
        "Delhi": 0, "Kolkata": 1, "Mumbai": 2,
        "Chennai": 3, "Bangalore": 4
    }
    dest_dict = {
        "Cochin": 0, "Delhi": 1, "New Delhi": 2,
        "Hyderabad": 3, "Kolkata": 4, "Bangalore": 5
    }
    stops_dict = {
        "non-stop": 0, "1 stop": 1, "2 stops": 2, "3 stops": 3, "4 stops": 4
    }

    input_data = np.array([[
        airline_dict[airline],
        source_dict[source],
        dest_dict[destination],
        stops_dict[total_stops],
        journey_day,
        journey_month,
        duration_mins,
        dep_hour,
        dep_min
    ]])

    return input_data

# Predict and display result
if st.button("Predict Price"):
    features = preprocess_input()
    prediction = model.predict(features)
    st.success(f"Estimated Ticket Price: ₹{int(prediction[0]):,}")
