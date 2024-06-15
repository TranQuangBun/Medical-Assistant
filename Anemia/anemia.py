from builtins import float

import streamlit as st
import sklearn
import pandas as pd
import numpy as np
import pickle
import joblib
from Authentication import account
from streamlit_option_menu import option_menu
from database import query


#def load_model():
   # with open('')
def app():
    st.title('Bạn đang dự đoán :red[THIẾU MÁU] 🩸')

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        choice = st.selectbox('Login/Signup', ['Đăng nhập', 'Tạo tài khoản'])
        if choice == 'Đăng nhập':
            # Email + Mật khẩu
            email = st.text_input('Địa chỉ Email', placeholder='Enter your email here ...')
            password = st.text_input('Mật khẩu', type='password', placeholder='Enter your password here ...')

            if st.button('Đăng nhập'):
                user = query.verify_credentials(email, password)
                if user:
                    # Lưu thông tin người dùng vào session state
                    st.success(f"Chào mừng, {user['name']}!")
                    st.balloons()
                    st.session_state['logged_in'] = {'logged_in': True, 'name': user['name'], 'email': user['email'],'phone': user['phone']}

                else:
                    st.error("Email hoặc mật khẩu không đúng!")

        elif choice == 'Tạo tài khoản':
            # Thêm các trường tạo tài khoản ở đây (ví dụ: tên, email, mật khẩu)
            name = st.text_input('Tên của bạn')
            email = st.text_input('Địa chỉ Email', placeholder='Enter your email here ...')
            phone = st.text_input('Số điện thoại')
            password = st.text_input('Mật khẩu', type='password', placeholder='Enter your password here ...')

            if st.button('Tạo tài khoản'):
                account.app()


    # Nếu người dùng đã đăng nhập, hiển thị thông tin người dùng
    if st.session_state.logged_in:
        with st.expander("Thông tin của bạn"):
            marks1, marks2, marks3 = st.columns(3, gap='large')
            with marks1:
                st.info('Người dùng', icon="👤")
                st.metric(label=st.session_state.logged_in['name'], value='')
            with marks2:
                st.info('Số điện thoại', icon="📞")
                st.metric(label=st.session_state.logged_in['phone'], value='')
            with marks3:
                st.info('Số lần test', icon="🧪")
            #   st.metric(label=user_data['test_count'], value='')



    # Chia trang web thành hai cột
    col1, spacer, col2 = st.columns([2, 1, 2])

#Bat dk nhap tai mooi input

    # Bên trái: 6 ô input
    with col1:
        st.header(":green[NHẬP SỐ LIỆU]")
        input1 = st.text_input(":green[1 - LYM] ")
        input2 = st.text_input(":green[2 - NEUT] ")
        input3 = st.text_input(":green[3 - MON] ")
        input4 = st.text_input(":green[4 - EOS] ")
        input5 = st.text_input(":green[5 - BASO ] ")
        input6 = st.text_input(":green[6 - HBG  ]")
        input7 = st.text_input(":green[7 - HCT ] ")
        input8 = st.text_input(":green[8 - MCV  ]")
        input9 = st.text_input(":green[9 - MCH ]")
        input10 = st.text_input(":green[10 - MCHC  ]")
        input11 = st.text_input(":green[11 - RDW  ] ")
        input12 = st.text_input(":green[12 - PLT  ] ")
        input13 = st.text_input(":green[13 - MPV  ] ")
        input14 = st.text_input(":green[14 - RBC  ] ")
        input15 = st.text_input(":green[15 - WBC  ] ")


    # Bên phải: layout hình chữ nhật với chú thích
    with col2:
        st.header(":green[Chú thích]")
        st.markdown(
            """
            <div style="border: 2px solid black; padding: 20px; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 12px;">
                <h3 style="font-size: 16px;">
                1. LYM (Lymphocyte – Bạch cầu Lympho): Lymphocyte là các tế bào có khả năng miễn dịch (thường từ 10% - 58.5%L). </br>
                2. NEUT (Neutrophil) - bạch cầu trung tính: Bạch cầu trung tính có chức năng quan trọng là thực bào (thường từ 37% - 80%M). </br>
                3. MON (monocyte) - bạch cầu mono: Mono bào là bạch cầu đơn nhân, sau sẽ biệt hóa thành đại thực bào (thường từ 0% - 12%M).  </br>
                4. EOS (eosinophils) - bạch cầu ái toan: Bạch cầu ái toan có khả năng thực bào yếu (thường từ 0.1% - 7%E).</br>
                5. BASO (basophils) - bạch cầu ái kiềm: Có vai trò quan trọng trong các phản ứng dị ứng (thường từ 0.1% - 2.5%).</br>
                6. HBG (Hemoglobin) – Lượng huyết sắc tố trong một thể tích máu (thường ở nam từ 12 - 18 g/dl, ở nữ từ 12 - 16 g/dl). </br>
                7. HCT (Hematocrit) – Tỷ lệ thể tích hồng cầu trên thể tích máu toàn phần (thường ở nam từ 45% - 51%, ở nữ từ 37% - 48%).</br>
                8. MCV (Mean corpuscular volume) – Thể tích trung bình của một hồng cầu (thường từ 80 - 97 fl).</br>
                9. MCH (Mean Corpuscular Hemoglobin) – Lượng huyết sắc tố trung bình trong một hồng cầu (thường từ 26 - 32 picogram(pg)).</br>
                10. MCHC (Mean Corpuscular Hemoglobin Concentration) – Nồng độ trung bình của huyết sắc tố hemoglobin trong một thể tích máu (thường từ 31% - 36%).</br>
                11. RDW (Red Cell Distribution Width) – Độ phân bố kích thước hồng cầu (thường từ 11.5% - 15.5%).</br>
                12. PLT (Platelet Count) – Số lượng tiểu cầu trong một thể tích máu (thường từ 140 - 440 K/uL).</br>
                13. MPV (Mean Platelet Volume) – Thể tích trung bình của tiểu cầu trong một thể tích máu (thường từ 0.0 - 99.8 fL)</br>
                </h3>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Thêm nút ở giữa phía dưới phần trên
    st.markdown("<br>", unsafe_allow_html=True)  # Thêm khoảng trắng để đẩy nút xuống dưới
    predict_button = st.columns(3)[1]  # Chia thành 3 cột và chọn cột giữa

    with predict_button:
        if st.button("Dự đoán bệnh"):
             model_load = joblib.load('Anemia/model_random_forest_classifier.sav')
             #model = pickle.load(open('Anemia/model_random_forest_classifier.sav','rb'))

             input_data = np.array([input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11, input12, input13,input14,input15])



             input_data = [float(x) for x in input_data]

             prediction = model_load.predict([input_data])
             prediction = [int(x) for x in prediction]
             query.insert_anemia(input1, input2, input3, input4, input5, input6, input7, input8, input9, input10,
                                 input11, input12, input13, input14, input15, prediction[0])

             if prediction[0] == 1:
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
                                                             <h4>⚠️ Mô hình dự đoán bệnh nhân BỊ mắc bệnh.</h4>                      
                                                         </div>
                                                     """, unsafe_allow_html=True)
             else:
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
                                       <h4>🎉 Mô hình dự đoán bệnh nhân KHÔNG mắc bệnh.</h4>
                                   </div>
                               """, unsafe_allow_html=True)






