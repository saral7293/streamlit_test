import streamlit as st
import requests

st.title('Iris Flower Prediction')

# Input features
sl = st.slider('Sepal Length', 4.0, 8.0, 5.1)
sw = st.slider('Sepal Width', 2.0, 4.5, 3.5)
pl = st.slider('Petal Length', 1.0, 7.0, 1.4)
pw = st.slider('Petal Width', 0.1, 2.5, 0.2)

# Update this URL to point to your deployed Flask API
url = 'https://irisflask-test.onrender.com/predict'

if st.button('Predict'):
    response = requests.post(url, json={'features': [sl, sw, pl, pw]})
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.success(f'The predicted Iris class is: {prediction}')
    else:
        st.error(f'Failed to get prediction: {response.text}')
