import streamlit as st

# Title of the app, centered alignment
st.markdown("<h1 style='text-align: center;'>Malicious URL Detector</h1>", unsafe_allow_html=True)

# Create a search bar with a label "Enter URL or Paste the URL"
search_query = st.text_input("Enter URL or Paste the URL:")

# Add a submit button
submit_button = st.button("Submit")

# Display the entered search query
if submit_button:
    st.write(f"You submitted: {search_query}")

