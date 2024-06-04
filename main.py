import pandas as pd
import streamlit as st
import pandas as pandas
import plotly.express as px
from streamlit_option_menu import  option_menu
from PIL import Image

from database import query

import home
from covid19 import covid19
from Anemia import anemia
from Authentication import account
import feedback


#navicon and header
logo = Image.open("Image/logo.png")
st.markdown("##")
#side bar
st.sidebar.image("Image/logo.png")

# Tạo sidebar với button
def run():

    with st.sidebar:
        app = option_menu(
            menu_title='MENU',
            options=['Home', 'Account', 'Blood', 'Covid19',"Feedback"],
            icons=['house-fill', 'person-circle','file-earmark-medical-fill','file-medical-fill','clipboard-heart-fill'],
            menu_icon='chat-text-fill',
            default_index=0,
            styles={
                "container": {"background-color": 'white'}, }
        )
    if app == "Home":
        home.Mark()
    if app == "Account":
        account.app()
    if app == "Blood":
        anemia.app()
    if app == "Covid19":
        covid19.app()
    if app == "Feedback":
        feedback.app()

run()



