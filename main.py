import streamlit as st
from streamlit_option_menu import  option_menu
from PIL import Image
from Diabetes import diabetes
from recommend import medicine
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
            options=['Home','Login/SignUp','Medicine Recommend', 'Blood', 'Covid19','Diabetes',"Feedback"],
            icons=['house-fill', 'person-circle','bi bi-clipboard-data','file-earmark-medical-fill','bi bi-lungs-fill','file-medical-fill','clipboard-heart-fill'],
            menu_icon='chat-text-fill',
            default_index=0,
            styles={
                "container": {"background-color": 'white'}, }
        )
        if 'logged_in' in st.session_state:
            if st.session_state.logged_in['is_logged']:
                if st.button("Đăng xuất"):
                    st.session_state.logged_in = {'is_logged': False, 'user_id': None, 'name': None, 'phone': None,
                                                  'email': None}
                    st.info("Đăng xuất Thành Công!!")
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = {'is_logged': False, 'user_id': None, 'name': None, 'phone': None,
                                      'email': None}
    if app == "Home":
        home.Mark()
    if app == "Login/SignUp":
        account.app()
    if app == "Medicine Recommend":
        medicine.app()
    if app == "Diabetes":
        diabetes.app()
    if app == "Blood":
        anemia.app()
    if app == "Covid19":
        covid19.app()
    if app == "Feedback":
        feedback.app()

run()



