

import streamlit as st
from utils.converter import convert_units
from utils.voice_output import speak_text
from theme import custom_css  # Importing theme from separate file

# Streamlit UI Settings
st.set_page_config(page_title="Unit Converter AI", page_icon="🔄", layout="wide")



# Apply Theme
st.markdown(custom_css, unsafe_allow_html=True)



# Title
st.title("Smart Unit Converter with Voice AI")



# Dropdown for unit categories
categories = {
    "Length": ["meter", "kilometer", "centimeter", "mile", "yard"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "milliliter", "gallon"],
    "Time": ["second", "minute", "hour", "day"],
}

category = st.selectbox(label="Select Category", options=list(categories.keys()))
from_unit = st.selectbox(label="From Unit", options=categories[category])
to_unit = st.selectbox(label="To Unit", options=categories[category])

# Input Field for Manual Entry
value = st.number_input(label="Enter Value", min_value=0.0, step=0.1, key="value_input")

# **Auto Conversion (No Button Needed)**


result = None
if value > 0:  # Convert only when a valid value is entered
    result = convert_units(value, from_unit, to_unit)

if result is not None:
    st.success(f"{value} {from_unit} = {result} {to_unit}")

# Button is always displayed
if st.button("🔊 Speak Output") and result is not None:
    speak_text(f"{value} {from_unit} is equal to {result} {to_unit}")

