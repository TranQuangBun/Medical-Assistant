import mysql.connector
from mysql.connector import Error
import streamlit as st

from database import query
def app():
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

        progress = ["Covid19", "Thiếu máu"]
        st.title(':red[Gửi phản hồi cho chúng tôi]  💖')
        selected_progress = st.selectbox("Bệnh đã dự đoán:", progress)
        feedback = st.text_area("Phản hồi:")

        # Phần giữa: Radio button
        st.title(":red[Phần lựa chọn 👇]")
        st.subheader("Bạn thấy dự đoán của chúng tôi như thế nào?")
        satisfaction_level_options = ["Dự đoán chính xác", "Dự đoán không chính xác"]
        satisfaction_level = st.radio("Mức độ hài lòng:", options=satisfaction_level_options)
        if st.button("Gửi phản hồi"):

            query.insert_feedback(selected_progress, feedback, satisfaction_level)

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
if __name__ == "__main__":
    app()
