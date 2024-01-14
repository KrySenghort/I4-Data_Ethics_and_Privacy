# page2.py
import streamlit as st
def page_about_us():
    st.title("About us")
    
    st.markdown("<h3 style='text-align: center;'>Member</h3>", unsafe_allow_html=True)
    
     # Display images in multiple columns
    col1, col2, col3, col4, col5 = st.columns(5)

    # Image 2
    img1 = "Project\images\phanit.jpg"
    col1.image(img1, caption="Nor Phanit(Data Collector)", use_column_width=True)

    # Image 2
    img2 = "Project\images\pbonat.jpg"
    col2.image(img2, caption="Ngeav Bonat(Data Analysis)", use_column_width=True)

    # Image 3
    img3 = "Project\images\senghort.jpg"
    col3.image(img3, caption="Kry Senghort(Manager and ML Engineer)", use_column_width=True)

    # Image 4
    img4 = "Project\images\pratha.jpg"
    col4.image(img4, caption="Phai Ratha(Presentation specialist)", use_column_width=True)

    # Image 5
    img5 = "Project\images\savin.jpg"
    col5.image(img5, caption="Run Savin(Report Specialist)", use_column_width=True)

    st.markdown(
    "We are all 4th-year students in the Department of Applied Mathematics and Statistics, majoring in data science. "
    "We have developed a system called <span style='color:red'>Fake News Detection using Natural Language Processing and Machine Learning</span> "
    "that can detect real or fake news with the specified truth level. Additionally, our goal is to build "
    "a system that can identify the authenticity of news in the form of text article to provide truthful level and reliable information, "
    "countering the harmful effects of fake news on society.",
    unsafe_allow_html=True
    )
    

