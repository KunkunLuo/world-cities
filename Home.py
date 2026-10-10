import streamlit as st

# Set page config
st.set_page_config(
    page_title="World Cities App",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Title and welcome section
st.title("🌍 World Cities Application")

st.write("""
Welcome to the World Cities App! This application allows you to explore and interact with city data from around the world.

### About This App
This multipage application provides tools and visualizations for discovering information about cities across the globe.

### Getting Started
Click the button below or navigate using the sidebar to access the main application features.
""")

# Navigation button
if st.button("📍 Go to Main App", use_container_width=True, type="primary"):
    st.switch_page("pages/app.py")

st.divider()

# Footer
st.markdown("""
---
*Navigate through the sidebar to access different sections of the application.*
""")
