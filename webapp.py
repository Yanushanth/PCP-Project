import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load your ML model (e.g., a trained model saved as 'model.pkl')
model = joblib.load('model.pkl')

# Function to predict if the URL is malicious
def predict_url(url):
    # Preprocess the URL and convert it to a feature vector suitable for the model
    # This is a placeholder; you'll need to use your actual preprocessing steps
    features = np.array([len(url)])  # Simple example: use URL length as a feature
    features = features.reshape(1, -1)
    prediction = model.predict(features)
    return prediction

# Navigation menu
menu = ["Home", "Profile", "Mission", "Project", "Contact", "About"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.markdown("<h1 style='text-align: center;'>Malicious URL Detector</h1>", unsafe_allow_html=True)

    # Create a search bar with a label "Enter URL or Paste the URL"
    search_query = st.text_input("Enter URL or Paste the URL:")

    # Add a submit button
    submit_button = st.button("Submit")

    # Display the entered search query and the prediction
    if submit_button:
        prediction = predict_url(search_query)
        st.write(f"You submitted: {search_query}")
        if prediction == 1:
            st.write("The URL is predicted to be malicious.")
        else:
            st.write("The URL is predicted to be safe.")
elif choice == "Profile":
    st.write("Profile Page")
    # Add content for the Profile page here
elif choice == "Mission":
    st.write("Mission Page")
    # Add content for the Mission page here
elif choice == "Project":
    st.write("Project Page")
    # Add content for the Project page here
elif choice == "Contact":
    st.write("Contact Page")
    # Add content for the Contact page here
elif choice == "About":
    st.write("About Page")
    # Add content for the About page here

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>© 2024 Malicious URL Detector. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)

