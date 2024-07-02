import streamlit as st
from geopy.geocoders import Nominatim

st.title("Address to Lat/Long")

address = st.text_input("Enter Address")

geolocator = Nominatim(user_agent="address-to-lat-long-app")
location = geolocator.geocode(address)

if address:
    st.write(f"Latitude: {location.latitude}")
    st.write(f"Longitude: {location.longitude}")
