import streamlit as st
from joblib import load

# Load the model
model = load('spam_detector_model.joblib')

st.title('Spam Detection')

# User input the text
user_input = st.text_area("Input the email content")

if st.button('Prediction'):
    prediction = model.predict([user_input])[0]
    if prediction == 1:
        st.write('This is spam.')
    else:
        st.write('This is not spam.')
