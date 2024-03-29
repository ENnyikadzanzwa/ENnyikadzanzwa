import streamlit as st
import pandas as pd
import base64

file_path = 'NyashaCV.pdf'

def get_binary_data(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return data

def download_pdf(binary_data, file_name):
    b64 = base64.b64encode(binary_data).decode('utf-8')
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}">Download PDF</a>'
    st.markdown(href, unsafe_allow_html=True)
pdf_binary_data = get_binary_data(file_path)

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
   st.image("mylog.png")
with b:
    if st.button("Download Emmanuel's CV"):
        download_pdf(pdf_binary_data, file_path)
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
              """, """Web development \n 
              DJango,Streamlit""", """Data Analysis\n
              Pandas,Plotly,Excel""",
              """Database systems\n
              Mysql""",]
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
    skills = ["Fundamentals of cybersecurity", """Artificial Intelligence \n
    Large language models,Fine tuning""", """Web Design\n
              HTML,CSS AND JAVASCRIPT""","APIs"]
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
        "description": "I have developed an AI Streamlit app that serves as a writing agent capable of generating various types of text such as emails, poems, and songs. The app uses natural language processing and machine learning techniques to understand user input and generate relevant and creative content. With this tool, users can easily create personalized and engaging written material for different purposes.",
        "link": "https://writing-agent-pbvdnbrsjsn6b6oxggn8by.streamlit.app/"
    },
    {
        "name": "Toy Store",
        "description": "This ecommerce website is built using HTML, CSS, and JavaScript. It allows users to browse a selection of toys and add them to their personal catalogue. Users can easily navigate through the website, select the toys they are interested in, and add them to their collection for purchase. The website provides a user-friendly experience for toy enthusiasts to explore and shop for their favorite items.",
        "link": "https://example.com/project2"
    },
    {
        "name": "Marketing Ad generator",
        "description": "Are you looking for an easy way to create marketing ads for your business? Look no further! With my AI Streamlit app, you can generate customized marketing ads by simply entering your business name, location, and type of business. Whether you're a small local shop or a large corporation, our app can help you create compelling ads to reach your target audience. Try it out today and take your marketing to the next level!",
        "link": "https://marketing-ad-generator-ksce6pgbarzkfz9xpbhtsx.streamlit.app/"
    }
]

for project in projects:
    st.write(f"**{project['name']}** ")
    st.write(f"{project['description']}") 
    st.write(f"{project['link']}")
   
    


st.header("Contact Me")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send"):
    st.write(f"Thank you {name}, your message has been sent!")




