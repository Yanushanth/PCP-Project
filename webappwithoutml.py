import streamlit as st

# Title of the app, centered alignment
st.markdown("<h1 style='text-align: center;'>Malicious URL Detector</h1>", unsafe_allow_html=True)

# Horizontal navigation menu
menu = ["Home", "Profile", "Mission", "Project", "Contact", "About"]
choice = st.selectbox("Navigation", menu)

if choice == "Home":
    # Create a search bar with a label "Enter URL or Paste the URL"
    search_query = st.text_input("Enter URL or Paste the URL:", key="home_search")

    # Add a submit button
    submit_button = st.button("Submit", key="home_submit")

    # Display the entered search query
    if submit_button:
        st.write(f"You submitted: {search_query}")
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

