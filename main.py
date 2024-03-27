import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Emmanuel nyikadzanzwa",
    page_icon="mylog.png",
    layout="centered",
    initial_sidebar_state="expanded",
    
    )
st.title("Emmanuel Nyasha Nyikadzanza's Profile")

st.write("""
**Name:** Emmanuel Nyasha Nyikadzanza\n
**Level:** 2.2\n
**Study:** Bachelor of Commerce Honours in Information Systems
""")
st.header("Skills")
skills = ["Python", "Django", "Data Analysis", "Machine Learning", "Web Development"]
for skill in skills:
    st.write(skill)
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
    st.write(f"**{project['name']}**")
    st.write(project['description'])
    st.write(f"[View Project]({project['link']})")


st.header("Contact Me")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send"):
    st.write(f"Thank you {name}, your message has been sent!")
st.header("Download Emmanuel's CV")
cv_url = "https://example.com/emmanuel_cv.pdf"
st.markdown(f"[Download CV]({cv_url})")


