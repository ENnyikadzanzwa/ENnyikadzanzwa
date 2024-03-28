import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Emmanuel nyikadzanzwa",
    page_icon="mylog.png",
    layout="centered",
    initial_sidebar_state="expanded",
    
    )

# Center the image
st.markdown(
    """
    <style>
    .reportview-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the image centered


# Display the title centered
st.markdown("<h1 style='text-align: center; color: blue;'>Software Developer</h1>", unsafe_allow_html=True)

col1,col2 = st.columns(2)
with col1:
    st.header("Bio")
    st.info("""
    **Name:** Emmanuel Nyasha Nyikadzanza\n
    **Level:** 2.2\n
    **Study:** Bachelor of Commerce Honours in Information Systems\n
    **Sex :** Male\n
    **D.O.B:**  29 November 2002\n
    **Marital status:** Single\n
    """)
with col2:
    st.image("mylog.png")
    st.header("What I do")
    st.info("""I am developing websites for both individuals and organizations that:\n
        - Seek to harness the capabilities of data analytics in their everyday operations.\n
        - Have encountered limitations with Excel and are seeking more efficient alternatives.\n
        - Face challenges in accounting and data manipulation, in search of improved solutions.\n
        - Desire a more convenient method for tracking and evaluating their business performance.
""")
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


