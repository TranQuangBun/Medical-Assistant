import streamlit as st

def app():
    progress = ["Covid19", "Thiếu máu"]

    # Phần đầu: Ô nhập thông tin
    st.title(':red[Gửi phản hồi cho chúng tôi]  💖')
    name = st.text_input("Họ và tên:")
    phone = st.text_input("Số điện thoại:")
    selected_progress = st.selectbox("Bệnh đã dự đoán:", progress)
    feedback = st.text_area("Phản hồi:")

    # Phần giữa: Radio button
    st.title(":red[Phần lựa chọn 👇]")
    st.subheader("Bạn thấy dự đoán của chúng tôi như thế nào?")
    satisfaction_level = st.radio("Mức độ hài lòng:",
                                  options=["Dự đoán chính xác", "Dự đoán không chính xác"])

    # Phần cuối: Button
    st.markdown("<br>", unsafe_allow_html=True)  # Thêm khoảng trắng để đẩy button xuống dưới
    if st.button("Gửi phản hồi"):
        st.success("Phản hồi của bạn đã được gửi đi.")

    # CSS để căn giữa phần header
    st.markdown(
         """
    <style>
    .css-2trqyj {
        display: flex;
        justify-content: center; 
    }
    </style>
    """,
        unsafe_allow_html=True
    )

