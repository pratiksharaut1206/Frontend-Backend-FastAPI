import streamlit as st
import requests ## <--- Importing requests library to make API calls

BACKEND_URL = "http://127.0.0.1:8000"  ## <--- URL of the FastAPI backend

st.title("FastAPI and Streamlit Integration")  ## <--- Setting the title of the Streamlit app
st.header("Welcome to the FastAPI and Streamlit Integration Demo")  ## <--- Adding a header to the app

if st.button("Call GET API"):

    response = requests.get(f"{BACKEND_URL}/hello")  ## <--- Making a GET request to the /hello endpoint

    data = response.json()  ## <--- Parsing the JSON response from the backend

    st.success(data["message"])  ## <--- Displaying the success message from the backend to the user


st.header("POST Request example")

name = st.text_input("Enter your name")

if st.button("Call POST API"):
    payload = {"name": name}  ## <--- Creating the payload for the POST request

    ## Final JSON: sent:
    '''
    {
        "name": "John"
    }
    '''
    response = requests.post(f"{BACKEND_URL}/greet", json=payload)  ## <--- Making a POST request to the /greet endpoint
    data = response.json()  ## <--- Parsing the JSON response from the backend

    st.success(data["response"])  ## <--- Displaying the success message from the backend to the user