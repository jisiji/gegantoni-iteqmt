# streamlit_app.py

import streamlit as st
import pandas as pd

# Title of the Streamlit app
st.title('Flower Classifier Results')

# Display the results
st.header('Results')

# Load results from results.txt
with open('results.txt', 'r') as f:
    results = f.read()

st.text(results)

# Display the dataset
st.header('Dataset')

# Load the dataset
df = pd.read_csv('/content/drive/MyDrive/Data/flowers.csv')
st.dataframe(df)
