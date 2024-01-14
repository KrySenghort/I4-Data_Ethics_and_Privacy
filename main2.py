import streamlit as st 
from login import page_login as login
from home import page_home as home
from about_us import page_about_us as about_us
from Execute import Execute as Execute
# from main import main as main

# ===============================================================================================
    
def main():
    st.sidebar.title("Section distributions")
    pages = {
        "Create Account":login,
        "Home": home,
        "Detect News":Execute,
        "About us": about_us
    }
    
    selected_page = st.sidebar.radio("Select a page", list(pages.keys()))
    page = pages[selected_page] 
    
    with st.spinner(f"Loading {selected_page} ..."):
        page()

# ==========================================
main()    


