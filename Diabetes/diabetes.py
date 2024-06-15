import streamlit as st

def app():
    st.info("DAI THAO DUONG")
    if st.session_state.logged_in:
        user_data = st.session_state.user_data
        with st.expander("Thông tin của bạn"):
            marks1, marks2, marks3 = st.columns(3, gap='large')
            with marks1:
                st.info('Người dùng', icon="👤")
                st.metric(label=user_data['name'], value='')
            with marks2:
                st.info('Số điện thoại', icon="📞")
                st.metric(label=user_data['phone'], value='')
            with marks3:
                st.info('Số lần test', icon="🧪")
            #   st.metric(label=user_data['test_count'], value='')
