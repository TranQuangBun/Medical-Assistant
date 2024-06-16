from builtins import float

import streamlit as st
import numpy as np
import joblib
from database import query

from streamlit_lottie import st_lottie
import requests

def app():
    st.title('Bạn đang dự đoán :red[THIẾU MÁU] 🩸')
    if 'logged_in' in st.session_state:
        if st.session_state.logged_in['is_logged']:
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
        else:
            st.info(":green[Model bạn đang sử dụng có độ chính xác là 93%!] Đăng nhập để sử dụng model chính xác hơn!!")


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
             model = None
             if 'logged_in' in st.session_state:
                 if st.session_state.logged_in['is_logged']:
                     model = joblib.load('./models/anemia/model_random_forest_classifier.sav')
                 else:
                     model = joblib.load('./models/anemia/model_logistic_regression.sav')

             input_data = np.array([input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11, input12, input13,input14,input15])

             input_data = [float(x) for x in input_data]

             prediction = model.predict([input_data])
             prediction = [int(x) for x in prediction]

             user_id = None
             if 'logged_in' in st.session_state:
                 if st.session_state.logged_in['is_logged']:
                     user_id = st.session_state.logged_in['user_id']

             query.insert_anemia(user_id,input1, input2, input3, input4, input5, input6, input7, input8, input9, input10,
                                 input11, input12, input13, input14, input15, prediction[0])

             if prediction[0] == 1:
                 def load_lottie_url(url: str):
                     r = requests.get(url)
                     if r.status_code != 200:
                         return None
                     return r.json()

                 lottie_animation = load_lottie_url(
                     "https://lottie.host/11bce142-1605-44a5-be30-3e96c5e02085/vyyX01ROgn.json")

                 col5, col6 = st.columns(2)
                 with col5:
                     if lottie_animation:
                         st_lottie(lottie_animation, height=200, width=200)
                     else:
                         st.write("Failed to load animation")
                 with col6:
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
                 def load_lottie_url(url: str):
                     r = requests.get(url)
                     if r.status_code != 200:
                         return None
                     return r.json()

                 lottie_animation = load_lottie_url(
                     "https://lottie.host/724a2c27-29da-48a2-8e64-0ba2a1a31d65/e30ugekdJ7.json")

                 col1, col2 = st.columns(2)

                 with col1:
                     if lottie_animation:
                         st_lottie(lottie_animation, height=200, width=200)
                     else:
                         st.write("Failed to load animation")

                 with col2:
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






