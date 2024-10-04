import streamlit as st

from forms.contact import contact_form






@st.dialog("Contact Me")
def showCont():
    contact_form()

links = st.Page( 
    page="views/bot.py",
    title="Bot",
    icon=":material/thumb_up:"
)

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")


with col1:
    st.image("./assets/Ola.png", width=230)
    
        
with col2:
    st.title("Ewuola Olaoluwakitan", anchor= False)
    st.write(
        "Full Stack Engineer, assisting enterprises by building best applications."
    )
    if st.button ("Contact Me"):
        showCont()

#Experience
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 3 Years experience in Building websites and web applications using ReactJS, Python, Php, TailwindCSS amongst others
    - Strong Hands on Experience and Knowledge in Python, SPSS and Excel
    - Good Understanding of Statistical Principles
    - Excellent Team Player and displaying a strong sense of initiative on tasks
    """
)
#Skills
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming:Python, HTML, CSS, Javascript, Php, SQL.
    - Data Visualization: MS Excel, SPSS.
    - Databases: Postgres, MongoDB, MySQL.
    """
)
