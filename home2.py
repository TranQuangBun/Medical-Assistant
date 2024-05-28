import streamlit as st
import mysql.connector


def verify_credentials(email, password):
    # Thực hiện kết nối đến MySQL
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3308",
            user="root",
            password="",
            db="bloodda"
        )

        # Tạo một con trỏ để thực hiện các truy vấn SQL
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM user WHERE email = %s AND password = %s"

        cursor.execute(query, (email, password))

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        # Trả về thông tin người dùng nếu đăng nhập thành công, None nếu không thành công
        return user

    except Exception as e:
        print("Error while connecting to MySQL", e)
        return None

# Trang đăng nhập

login_placeholder = st.empty()
# Login page
def login_page():
    email = st.text_input("Email")
    password = st.text_input("Mật khẩu", type="password")

    if st.button("Đăng nhập"):
        user = verify_credentials(email, password)
        if user:
            # Lưu thông tin người dùng vào session state
            st.session_state.user_data = user
            # Đặt session_state.logged_in thành True
            st.session_state.logged_in = True
            # Ẩn phần đăng nhập
            login_placeholder.empty()

# Home page
def home_page():
    # Kiểm tra xem người dùng đã đăng nhập chưa
    if st.session_state.get("logged_in"):
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

        st.markdown("""---""")
    else:
        st.warning("Bạn cần đăng nhập trước khi xem trang này.")

# Hàm chính
def main():
    # Đảm bảo rằng session_state.logged_in được khởi tạo
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Hiển thị trang đăng nhập
    login_page()

    # Hiển thị trang chính nếu người dùng đã đăng nhập thành công
    if st.session_state.logged_in:
        home_page()

if __name__ == "__main__":
    main()