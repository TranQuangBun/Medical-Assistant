import streamlit as st
from traitlets import link
import matplotlib.pyplot as plt
from Authentication import account
from database import query
import pandas as pd
from PIL import Image

news = query.get_news()
data = query.view_all_data()
css = """
<style>
.image-container {
  display: flex;
  justify-content: center;
}
</style>
"""
def Mark():
    st.title('Chào mừng bạn đến :red[BLOOD TEST 🩸]')
  # account.app()
    with st.expander("CÁC BỆNH CHÚNG TÔI CÓ THỂ DỰ ĐOÁN"):
        marks1, marks2 = st.columns(2, gap='large')
        with marks1:
            st.info(':red[Phát hiện thiếu máu]', icon="🩸")
            st.image('Image/thieumau.jpg', width=300)
        with marks2:
            st.info(':red[Đánh giá nguy cơ COVID-19]', icon="🦠")
            st.image('Image/covid.jpg', width=300)
    st.info(":green[Đối tượng sử dụng :]"
               " Trang web này hướng đến những người muốn theo dõi sức khỏe của bản thân, đặc biệt là những người có nguy cơ mắc thiếu máu hoặc COVID-19.\n")
    st.info(":green[Lợi ích:]"
               " Giúp phát hiện sớm các bệnh lý nguy hiểm."
               " Theo dõi sức khỏe một cách hiệu quả."
               " Tiết kiệm thời gian và chi phí.")

    st.info("👉 Hãy truy cập trang web của chúng tôi để phân tích bảng xét nghiệm máu toàn phần và bảo vệ sức khỏe của bạn!")

    # Chia thành hai cột

    left_column, spacer, right_column = st.columns([2, 1, 2])
    # Cột bên trái
    with right_column:
        st.subheader('📊 :red[BIỂU ĐỒ]')
        # Dữ liệu mẫu
        # Dữ liệu mẫu
        data = {
            'LYM': [13.4, 17.7],
            'NEUT': [73.7, 73.5],
            'MONO': [9.5, 7.2],
            'EOS': [2.9, 0.1],
            'BASO': [0.5, 0.2],
            'HGB': [13.2, 14.9],
            'HCT': [38.5, 42.7],
            'MCV': [100.8, 82.0],
            'MCH': [34.7, 28.6],
            'MCHC': [34.4, 34.9],
            'RDW': [12.8, 12.5],
            'PLT': [200.5, 337.0],
            'MPV': [9.9, 10.1],
            'diseased': [0, 1]
        }

        # Tạo DataFrame từ dữ liệu
        df = pd.DataFrame(data)

        # Tách dữ liệu thành hai nhóm: diseased và non-diseased
        df_diseased = df[df['diseased'] == 1]
        df_non_diseased = df[df['diseased'] == 0]

        # Loại bỏ cột 'diseased' để vẽ biểu đồ
        df_diseased = df_diseased.drop(columns=['diseased'])
        df_non_diseased = df_non_diseased.drop(columns=['diseased'])

        # Hàm để vẽ biểu đồ cho nhóm không bệnh
        def plot_non_diseased(df_non_diseased):
            fig, ax = plt.subplots(figsize=(20, 12))  # Tăng kích thước biểu đồ

            # Vẽ biểu đồ cho nhóm không bệnh
            df_non_diseased.T.plot(kind='bar', ax=ax, color='blue', alpha=0.6, position=1, width=0.4,
                                   label='Non-Diseased')

            # Cài đặt nhãn và tiêu đề
            ax.set_xlabel('Blood Indices', fontsize=16)  # Tăng kích thước phông chữ nhãn trục X
            ax.set_ylabel('Values', fontsize=16)  # Tăng kích thước phông chữ nhãn trục Y
            ax.set_title('Blood Indices of Non-Diseased Individuals', fontsize=20)  # Tăng kích thước phông chữ tiêu đề
            ax.legend(['Non-Diseased'], fontsize=14)  # Tăng kích thước phông chữ chú giải

            plt.xticks(rotation=45, fontsize=14)  # Tăng kích thước phông chữ nhãn trục X
            plt.yticks(fontsize=14)  # Tăng kích thước phông chữ nhãn trục Y
            st.pyplot(fig)

        # Hàm để vẽ biểu đồ cho nhóm bệnh
        def plot_diseased(df_diseased):
            fig, ax = plt.subplots(figsize=(20, 12))  # Tăng kích thước biểu đồ

            # Vẽ biểu đồ cho nhóm bệnh
            df_diseased.T.plot(kind='bar', ax=ax, color='red', alpha=0.6, position=0, width=0.4, label='Diseased')

            # Cài đặt nhãn và tiêu đề
            ax.set_xlabel('Blood Indices', fontsize=16)  # Tăng kích thước phông chữ nhãn trục X
            ax.set_ylabel('Values', fontsize=16)  # Tăng kích thước phông chữ nhãn trục Y
            ax.set_title('Blood Indices of Diseased Individuals', fontsize=20)  # Tăng kích thước phông chữ tiêu đề
            ax.legend(['Diseased'], fontsize=14)  # Tăng kích thước phông chữ chú giải

            plt.xticks(rotation=45, fontsize=14)  # Tăng kích thước phông chữ nhãn trục X
            plt.yticks(fontsize=14)  # Tăng kích thước phông chữ nhãn trục Y
            st.pyplot(fig)

        # Gọi hàm plot_non_diseased và plot_diseased để vẽ hai biểu đồ riêng biệt
        st.header('Người không mắc bệnh')
        plot_non_diseased(df_non_diseased)
        st.header('Người bị bệnh')
        plot_diseased(df_diseased)
    # Cột bên trái
    with left_column:
        st.subheader('📰 :red[TIN TỨC]')
        for title, content, image_url, link in news:
            link_test = link
            title_test = title
            st.markdown(f"[**{title_test}**]({link_test})", unsafe_allow_html=False)
            if image_url:
                img_path = "Image/" + image_url
                image = Image.open(img_path)
                st.image(image, caption=content, use_column_width=True)

            else:
                st.write(content)





