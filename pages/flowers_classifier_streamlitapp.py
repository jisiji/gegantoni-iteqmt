import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Title of the Streamlit app
st.title("Flower Lifespan Predictor")

# Input features from the user
max_height = st.number_input("Maximum Height (cm):", min_value=0.0, step=0.1)
min_height = st.number_input("Minimum Height (cm):", min_value=0.0, step=0.1)
num_petals = st.number_input("Number of Petals:", min_value=0, step=1)

# Sample data for demonstration purposes
data = {
    'max_height': [15, 30, 22, 45, 35, 10, 50, 25, 40, 20],
    'min_height': [10, 20, 15, 35, 25, 5, 45, 20, 30, 15],
    'num_petals': [5, 7, 6, 8, 7, 4, 9, 6, 7, 5],
    'lifespan': [2, 3, 2.5, 4, 3.5, 1, 5, 2.8, 3.7, 2.2]  # Lifespan in weeks
}

# Convert the sample data into a DataFrame
df = pd.DataFrame(data)

# Split the data into features and target
X = df[['max_height', 'min_height', 'num_petals']]
y = df['lifespan']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Function to make predictions
def predict_lifespan(max_height, min_height, num_petals):
    input_data = np.array([[max_height, min_height, num_petals]])
    prediction = model.predict(input_data)
    return prediction[0]

# Button to trigger the prediction
if st.button("Predict Lifespan"):
    if max_height == 0 or min_height == 0 or num_petals == 0:
        st.write("Please enter valid values for all features.")
    else:
        predicted_lifespan = predict_lifespan(max_height, min_height, num_petals)
        st.write(f"The predicted lifespan of the flower is: {predicted_lifespan:.2f} weeks")
