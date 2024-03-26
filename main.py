import streamlit as st
st.set_page_config(
    page_title="Digital Resume",
    page_icon="mylog.png",
    layout="centered",
    initial_sidebar_state="expanded",
    
    )
col1,col2 = st.columns(2)
with col1:
    st.image("mylog.png")
with col2:
    st.header(":green[Emmanuel Nyasha Nyikadzanzwa]")
    st.markdown(">email nyikadzanzwaemmanuelnyasha@gmail.com")

    col,co,c3 = st.columns(3)
    with col:
        st.markdown("> :orange[facebook]")
    with co:
        st.markdown("> :green[whatsapp]")
    with c3:
        st.markdown("> :orange[github]")

st.subheader(":green[Junior Software Developer]")
st.markdown("---")
st.subheader("About")
st.info(""" -This example includes three HTML pages (index.html, products.html, contact.html),
         -a CSS file (styles.css) for styling, and an empty JavaScript file (script.js) 
        - for potential additional functionality. 
         -The navigation bar at the bottom of each page allows users to navigate between
          - the home page, products page, and contact page. Products are displayed in categories
         -vertically aligned on the products page. """)
st.subheader("Skills")
st.info(""" -This example includes three HTML pages (index.html, products.html, contact.html),
         -a CSS file (styles.css) for styling, and an empty JavaScript file (script.js) 
        - for potential additional functionality. 
         -The navigation bar at the bottom of each page allows users to navigate between
          - the home page, products page, and contact page. Products are displayed in categories
         -vertically aligned on the products page. """)
st.subheader("Projects")
st.info(""" -This example includes three HTML pages (index.html, products.html, contact.html),
         -a CSS file (styles.css) for styling, and an empty JavaScript file (script.js) 
        - for potential additional functionality. 
         -The navigation bar at the bottom of each page allows users to navigate between
          - the home page, products page, and contact page. Products are displayed in categories
         -vertically aligned on the products page. """)