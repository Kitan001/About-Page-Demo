import streamlit as st

#PAGE SETUP
about= st.Page(
    page="views/about.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
projectPage = st.Page(
    page="views/dashboard.py",
    title="My Dashboard",
    icon=":material/bar_chart:",
)
botPage = st.Page( 
    page="views/bot.py",
    title="Bot",
    icon=":material/smart_toy:"
)

#Navigation
#pg= st.navigation(pages=[about,projectPage,botPage ])

pg=st.navigation(
    {
        "Info": [about],
        "Projects": [projectPage,botPage]
    }
)

st.logo("assets/dove.png")
st.sidebar.text("Made by Olaoluwakitan")


pg.run()