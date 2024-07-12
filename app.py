import streamlit as st
import requests
from datetime import datetime

'''
# TaxiFareModel front
'''
date = st.date_input("Select the date of the ride", datetime.now())
time = st.time_input("Select the time of the ride", datetime.now().time())
pickup_longitude = st.number_input("Enter pickup longitude", format="%.6f")
pickup_latitude = st.number_input("Enter pickup latitude", format="%.6f")
dropoff_longitude = st.number_input("Enter dropoff longitude", format="%.6f")
dropoff_latitude = st.number_input("Enter dropoff latitude", format="%.6f")
passenger_count = st.number_input("Enter number of passengers", min_value=1, max_value=10, step=1)

pickup_datetime = datetime.combine(date, time)
pickup_datetime_str = pickup_datetime.strftime("%Y-%m-%d %H:%M:%S")





url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

params = {
    "key": "2012-10-06 12:10:20.0000001",
    "pickup_datetime": pickup_datetime_str,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

if st.button('Get Fare Prediction'):
    # Call the API using the requests package
    response = requests.get(url, params=params)

    # Retrieve the prediction from the JSON returned by the API
    if response.status_code == 200:
        prediction = response.json().get("fare", "Error: No prediction found")
        st.write(f"The predicted fare is: ${prediction:.2f}")
    else:
        st.write("Error: Failed to retrieve prediction")
