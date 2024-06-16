
import streamlit as st
from database import query
def app():

    if 'logged_in' in st.session_state:
        if st.session_state.logged_in['is_logged']:

            progress = ["Covid19", "Thiếu Máu","Đái Tháo Đường"]
            st.title(':red[Gửi phản hồi cho chúng tôi]  💖')
            user = {'name': st.session_state.logged_in['name'], 'phone': st.session_state.logged_in['phone'],
                    'email': st.session_state.logged_in['email']}
            with st.expander("Thông tin của bạn"):
                marks1, marks2, marks3 = st.columns(3, gap='large')
                with marks1:
                    st.info(user['name'], icon="👤")
                with marks2:
                    st.info(user['phone'], icon="📞")
                with marks3:
                    st.info('Số lần test', icon="🧪")
            selected_progress = st.selectbox("Bệnh đã dự đoán:", progress)
            feedback = st.text_area("Phản hồi:")

            # Phần giữa: Radio button
            st.title(":red[Phần lựa chọn 👇]")
            st.subheader("Bạn thấy dự đoán của chúng tôi như thế nào?")
            satisfaction_level_options = ["Dự đoán chính xác", "Dự đoán không chính xác"]
            satisfaction_level = st.radio("Mức độ hài lòng:", options=satisfaction_level_options)
            if st.button("Gửi phản hồi"):
                if 'logged_in' in st.session_state:
                    if st.session_state.logged_in['is_logged']:
                        user_id = st.session_state.logged_in['user_id']

                query.insert_feedback(user_id,selected_progress, feedback, satisfaction_level)

                st.markdown("""
                            <style>
                            .success-box {
                                padding: 20px;
                                border-radius: 10px;
                                background-color: #f0f8ff;
                                color: #006400;
                                font-size: 18px;
                                width: 400px;
                                margin: 0 auto;
                                text-align: center;
                                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                            }
                            .success-box h4 {
                                margin-top: 0;
                                font-size: 24px;
                                color: #006400;
                            }
                            .success-box p {
                                margin-bottom: 0;
                            }
                            </style>
                            <div class="success-box">
                                <h4>🎉 Phản hồi đã được gửi!</h4>
                                <p>Cảm ơn bạn đã sử dụng dịch vụ dự đoán của chúng tôi!</p>
                            </div>
                        """, unsafe_allow_html=True)
                st.balloons()
        else:
            st.info("Hãy đăng nhập để phản hồi!!")


if __name__ == "__main__":
    app()
