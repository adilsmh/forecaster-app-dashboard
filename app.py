import streamlit as st
import pandas as pd
import requests

# Set up the app
st.title("Sales Prediction App")

# Define the API endpoint
API_ENDPOINT = "http://forecasterapi.azurewebsites.net/forecast"

# Define a function to generate the predictions
def generate_predictions(num_weeks):
    # Make a request to the API to get the predictions
    response = requests.get(f"{API_ENDPOINT}/{num_weeks}")
    
    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to a pandas dataframe
        data = response.json()
        df = pd.DataFrame(data)
        
        return df
    else:
        st.error("Failed to generate predictions. Please try again later.")
        return None

# Define the list of available products
product_list = ["product1", "product2", "product3"]

# Define the default number of weeks to predict
num_weeks = 4

# Add widgets to the app to allow the user to select the products and number of weeks to predict
selected_products = st.multiselect("Select products", product_list)
num_weeks = st.slider("Number of weeks to predict", min_value=1, max_value=12, value=num_weeks)

# Add a button to trigger the prediction
if st.button("Predict"):
    # Generate the predictions and display the results
    predictions_df = generate_predictions(num_weeks)
    if predictions_df is not None:
        st.line_chart(predictions_df, x="date", y="forecasted_number_of_products")
        st.write(predictions_df)
