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

a,b = st.columns(2)
with a:
    st.write("   ")
with b:
    st.image("mylog.png")
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
    st.header(" Hard Skills")
    skills = ["""Programming languages\n
              Python C#\n
              """, "Web development\nDJango,Streamlit", "Data Analysis\n Pandas,Plotly", "AI and ML\nLarge language models", "Web Design\nHTML,CSS AND JAVASCRIPT","Database systems\nMysql",]
    for skill in skills:
        st.info(skill)
with col2:
    
    st.header("What I do")
    st.info("""I am developing websites for both individuals and organizations that:\n
        - Seek to harness the capabilities of data analytics in their everyday operations.\n
        - Have encountered limitations with Excel and are seeking more efficient alternatives.\n
        - Face challenges in accounting and data manipulation, in search of improved solutions.\n
        - Desire a more convenient method for tracking and evaluating their business performance.
    """)
    st.header("Other Skills")
    skills = ["Fundamentals of cybersecurity", "Networking", "APIs", "Web Development"]
    for skill in skills:
        st.info(skill)


st.header("Projects")
projects = [
    {
        "name": "Online electricity scheduling ssystem",
        "description": """The online electricity scheduling system project built on Streamlit aims to provide a user-friendly platform for managing and scheduling electricity usage. This system allows users to view real-time electricity consumption data, schedule power usage for different appliances, and optimize energy usage to reduce costs and environmental impact. The interface is designed to be intuitive and easy to navigate, allowing users to monitor their electricity usage patterns and make informed decisions about their energy consumption. Additionally, the system may include features such as predictive analytics to forecast energy demand, integration with smart home devices for automated scheduling, and customizable reporting for tracking usage trends. Overall, 
        the project aims to streamline electricity management for both residential and commercial users, promoting efficient and sustainable energy practices.""",
        "link": "https://onlineelectricityschedulingsystem.streamlit.app/"
    },
    {
        "name": "Writing agent",
        "description": "A brief description of Project 2.",
        "link": "https://writing-agent-pbvdnbrsjsn6b6oxggn8by.streamlit.app/"
    },
    {
        "name": "Toy Store",
        "description": "A brief description of Project 2.",
        "link": "https://example.com/project2"
    },
    {
        "name": "Marketing Ad generator",
        "description": "A brief description of Project 2.",
        "link": "https://marketing-ad-generator-ksce6pgbarzkfz9xpbhtsx.streamlit.app/"
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


