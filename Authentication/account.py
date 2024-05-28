import streamlit as st
import mysql.connector
from database import query
import streamlit as st
import home


def app():
    st.title('Chào mừng bạn đến :red[BLOOD TEST] 🩸')

    choice = st.selectbox('Login/Signup', ['Đăng nhập', 'Tạo tài khoản'])
    if choice == 'Đăng nhập':
        # Email + Pass
        email = st.text_input('Địa chỉ Email', placeholder='Enter your username here ...')
        password = st.text_input('Mật khẩu', type='password', placeholder='Enter your password here ...')

        if st.button('Đăng nhập'):
            user = query.verify_credentials(email, password)
            if user:
                # Lưu thông tin người dùng vào session state
                st.session_state.user_data = user
                st.session_state.logged_in = True
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
                st.markdown("""
                       <style>
                       .error-box {
                           padding: 10px;
                           border: 2px solid red;
                           border-radius: 5px;
                           background-color: #f8d7da;
                           color: red;
                           font-size: 16px;
                       }
                       </style>
                       <div class="error-box">
                           <h4>⚠️ Lỗi đăng nhập</h4>
                           <p>Có vấn đề với tài khoản hoặc mật khẩu của bạn ! </p>
                       </div>
                   """, unsafe_allow_html=True)


    else:
        # need phone
        name = st.text_input('Tên người dùng')
        email = st.text_input('Địa chỉ Email')
        phone = st.text_input('Số điện thoại')
        password = st.text_input('Mật khẩu', type='password')

        if st.button('Tạo tài khoản'):
            sql = "insert into user(name,email,phone,password) values(%s,%s,%s,%s)"
            val = (name, email, phone, password)
            query.mycursor.execute(sql, val)
            query.conn.commit()
            st.markdown("""
                  <style>
                  .success-box {
                      padding: 10px;
                      border: 2px solid green;
                      border-radius: 5px;
                      background-color: #dff0d8;
                      color: green;
                      font-size: 16px;
                  }
                  </style>
                  <div class="success-box">
                      <h4>🎉 Success!</h4>
                      <p>Tài khoản của bạn đã được tạo thành công. Bây giờ bạn có thể đăng nhập bằng tài khoản mới của mình.</p>
                  </div>
              """, unsafe_allow_html=True)
