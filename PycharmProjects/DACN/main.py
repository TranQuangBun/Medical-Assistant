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

#navicon and header
logo = Image.open("Image/logo.png")
st.set_page_config(page_title="Dashboard", page_icon="🩸", layout="wide")
st.subheader("🔔 Blood Predict")
app = option_menu(
        menu_title='MENU Progress',
        options=['Blood', 'Covid19'],
        icons=['file-earmark-medical-fill', 'file-medical-fill'],
        menu_icon='chat-text-fill',
        default_index=0,
        orientation="v"
    )
st.markdown("##")
#id count

# covid 19 data
result = query.view_all_data()
df=pd.DataFrame(result,columns=["ID", "sex", "age", "pcr_date", "exam_bh_date","leukocytes", "neutrophilsP", "lymphocytesP", "monocytesP", "eosinophilsP",
    "basophilsP", "neutrophils", "lymphocytes", "monocytes", "eosinophils",
    "basophils", "redbloodcells", "mcv", "mch", "mchc", "rdwP",
    "hemoglobin", "hematocritP", "platelets", "mpv", "pcr"])
#side bar
st.sidebar.image("Image/logo.png")

# Tạo sidebar với button
def run():

    with st.sidebar:
        app = option_menu(
            menu_title='MENU',
            options=['Home', 'Account', 'Blood', 'Covid19'],
            icons=['house-fill', 'person-circle','file-earmark-medical-fill','file-medical-fill'],
            menu_icon='chat-text-fill',
            default_index=0,
            styles={
                "container": {"background-color": 'white'}, }
        )
    if app == "Home":
        st.subheader(f"Trang: {app}")
        home.app()
    if app == "Account":
        st.subheader(f"Trang: {app}")
        account.app()
    if app == "Blood":
        st.subheader(f"Trang: {app}")
        anemia.app()
    if app == "Covid19":
        st.subheader(f"Trang: {app}")
        covid19.app()

def Home():
    with st.expander("Tabular"):
      # df_selection = df.query()
       marks1,marks2,marks3,marks4 =st.columns(4,gap='large')
       with marks1:
           st.info('Thong tin data',icon="📌")
           st.metric(label="123",value=f"{query.count_id()}")
       with marks2:
           st.info('Thong tin data',icon="📌")
           st.metric(label="123",value=f"")
       with marks3:
           st.info('Thong tin data',icon="📌")
           st.metric(label="123",value=f"")
       with marks4:
           st.info('Thong tin data',icon="📌")
           st.metric(label="123",value=f"")

       st.markdown("""---""")
run()
Home()


