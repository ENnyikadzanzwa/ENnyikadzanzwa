import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Emmanuel nyikadzanzwa",
    page_icon="mylog.png",
    layout="centered",
    initial_sidebar_state="expanded",
    
    )
st.title("Emmanuel Nyasha Nyikadzanza's Profile")

col1,col2 = st.columns(2)
with col1:
    st.info("""
    **Name:** Emmanuel Nyasha Nyikadzanza\n
    **Level:** 2.2\n
    **Study:** Bachelor of Commerce Honours in Information Systems
    """)
with col2:
    st.header("What I do")
    st.info("looking at ")
st.header("Skills")
skills = ["Python", "Django", "Data Analysis", "Machine Learning", "Web Development"]
for skill in skills:
    st.info(skill)
st.header("Projects")
projects = [
    {
        "name": "Project 1",
        "description": "A brief description of Project 1.",
        "link": "https://example.com/project1"
    },
    {
        "name": "Project 2",
        "description": "A brief description of Project 2.",
        "link": "https://example.com/project2"
    }
]

for project in projects:
    st.info(f"""**{project['name']}** \n 
    {project['description']} \n 
    [View Project]({project['link']})""")
    


st.header("Contact Me")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send"):
    st.write(f"Thank you {name}, your message has been sent!")
st.header("Download Emmanuel's CV")
cv_url = "https://example.com/emmanuel_cv.pdf"
st.markdown(f"[Download CV]({cv_url})")


