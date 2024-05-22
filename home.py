import streamlit as st
from traitlets import link

from database import query
import pandas as pd
from PIL import Image

news = query.get_news()
data = query.view_all_data()
def Mark():
    st.title('Chào mừng bạn đến :red[BLOOD TEST 🩸]')

    with st.expander("Thông tin của bạn"):
       marks1,marks2,marks3 =st.columns(3,gap='large')
       with marks1:
           st.info('Người dùng',icon="👤")
          # st.metric(label="#", value=user_data)
       with marks2:
           st.info('Số điện thoại',icon="📞")
          # st.metric(label="#", value=user_data)
       with marks3:
           st.info('Số lần test',icon="🧪")
         #  st.metric(label="#", value=user_data)

       st.markdown("""---""")

    # Chia thành hai cột

    left_column, spacer, right_column = st.columns([2, 1, 2])
    # Cột bên trái
    with right_column:
        st.subheader('📊 :red[BIỂU ĐỒ]')
        st.bar_chart(data.set_index('pcr_date'))

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




