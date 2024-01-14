import streamlit as st
def page_login():
    
    st.markdown("<h1 style='text-align: center;'>Create Account</h1>", unsafe_allow_html=True)

    # Input form
    name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")
    sex = st.selectbox("Enter your gender:", ["female", "male"])
    career = st.selectbox("Enter your career:", [
        "Software Developer", "Data Scientist", "Teacher", "Nurse", "Doctor", "Graphic Designer",
        "Marketing Manager", "Financial Analyst", "Chef", "Photographer", "Journalist", "Electrician",
        "Mechanical Engineer", "Fitness Trainer", "Architect", "Police Officer", "Real Estate Agent",
        "Event Planner", "Social Worker", "Dentist", "Librarian", "Fashion Designer", "Biologist",
        "Flight Attendant", "Sales Representative", "Psychologist", "Pharmacist", "Translator",
        "Web Designer", "HR Manager", "Electrician", "Plumber", "Veterinarian", "Construction Worker",
        "Pilot", "Geologist", "Interior Designer", "IT Consultant", "Legal Assistant", "Meteorologist",
        "Phlebotomist", "Radiologist", "Speech Therapist", "Social Media Manager", "Technical Writer",
        "Zoologist", "Forensic Scientist", "Landscape Architect"
    ])

    # Check if all information is provided
    if name and email and sex and career:
        # Store user information in session state
        st.session_state.user_info = {
            "name": name,
            "email": email,
            "sex": sex,
            "career": career
        }

        # Submit button
        if st.button("Submit"):
            # Redirect to another page (e.g., dashboard)
            st.experimental_rerun()
    else:
        st.warning("Please provide all required information.")
