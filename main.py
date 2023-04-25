"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st
import pandas as pd

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, data, predict, visualise, predict_unseen_data

# Configure the app
st.set_page_config(
    page_title = 'A-18 Parkinson\'s Disease Prediction',
    page_icon = 'raised_hand_with_fingers_splayed',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "Dataset Info": data,
    "Prediction": predict,
    "Visualisation": visualise,
    "Prediction on Unseen Data": predict_unseen_data
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Menu")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))


# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction", "Visualisation", "Prediction on Unseen Data"]:
    Tabs[page].app(df, X, y)
elif (page == "Dataset Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
