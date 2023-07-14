import streamlit as st
import boto3
import gspread
from google.oauth2 import service_account
import base64
from PIL import Image
from io import BytesIO


### settings ###

st.set_page_config(
    page_title="JiRO.com",
    page_icon="🏫"  
)

st.markdown(
    """
    <style>
    .padding {
        padding: 10px;
        border: 1px solid lightgrey;
        background-color: white;
        border-radius: 5px;
        color; 1px solid lightgrey;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .full-width-button {
        width: 100%;
        box-sizing: border-box;
    }
    </style>
    """,
    unsafe_allow_html=True
)

###########################################################################################################
# 데이터 저장
###########################################################################################################

credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])
client = gspread.authorize(credentials)
spreadsheet = client.open_by_key('1EdBRIDn1YOT44TApVf7w4ueR8GkHOdiZln7UF3vcO0M')
worksheet = spreadsheet.sheet1
data = worksheet.get_all_values()

###########################################################################################################
# 글 데이터 로드
###########################################################################################################

p1_list = []
p1_encodedimagelist = []
p1_titlelist1 = []
p1_textlist1 = []
p1_encodedimagelist1 = []
p1_titlelist2 = []
p1_textlist2 = []
p1_encodedimagelist2 = []
p1_titlelist3 = []
p1_textlist3 = []
p1_encodedimagelist3 = []
p1_titlelist4 = []
p1_textlist4 = []
p1_encodedimagelist4 = []
p1_titlelist5 = []
p1_textlist5 = []
p1_encodedimagelist5 = []
p1_titlelist6 = []
p1_textlist6 = []
p1_encodedimagelist6 = []
p1_titlelist7 = []
p1_textlist7 = []
p1_encodedimagelist7 = []
p1_titlelist8 = []
p1_textlist8 = []
p1_encodedimagelist8 = []
p1_titlelist9 = []
p1_textlist9 = []
p1_encodedimagelist9 = []
p1_titlelist10 = []
p1_textlist10 = []
p1_encodedimagelist10 = []
p1_titlelist11 = []
p1_textlist11 = []
p1_encodedimagelist11 = []

for row in data:
    if row[3] == "건축":
        p1_titlelist1.append(row[0])
        p1_textlist1.append(row[1])
        p1_encodedimagelist1.append(row[4])

    elif row[3] == "교통·운송":
        p1_titlelist2.append(row[0])
        p1_textlist2.append(row[1])
        p1_encodedimagelist2.append(row[4])

    elif row[3] == "기계·금속":
        p1_titlelist3.append(row[0])
        p1_textlist3.append(row[1])
        p1_encodedimagelist3.append(row[4])

    elif row[3] == "산업":
        p1_titlelist4.append(row[0])
        p1_textlist4.append(row[1])
        p1_encodedimagelist4.append(row[4])

    elif row[3] == "소재·재료":
        p1_titlelist5.append(row[0])
        p1_textlist5.append(row[1])
        p1_encodedimagelist5.append(row[4])

    elif row[3] == "전기·전자":
        p1_titlelist6.append(row[0])
        p1_textlist6.append(row[1])
        p1_encodedimagelist6.append(row[4])

    elif row[3] == "정밀·에너지":
        p1_titlelist7.append(row[0])
        p1_textlist7.append(row[1])
        p1_encodedimagelist7.append(row[4])

    elif row[3] == "컴퓨터·통신":
        p1_titlelist8.append(row[0])
        p1_textlist8.append(row[1])
        p1_encodedimagelist8.append(row[4])

    elif row[3] == "토목·도시":
        p1_titlelist9.append(row[0])
        p1_textlist9.append(row[1])
        p1_encodedimagelist9.append(row[4])

    elif row[3] == "화공":
        p1_titlelist10.append(row[0])
        p1_textlist10.append(row[1])
        p1_encodedimagelist10.append(row[4])

    elif row[3] == "기타":
        p1_titlelist11.append(row[0])
        p1_textlist11.append(row[1])
        p1_encodedimagelist11.append(row[4])




###########################################################################################################
# sidebar
###########################################################################################################


###########################################################################################################
# main page 
###########################################################################################################

st.markdown('<h3 style="text-align: center;">공학계열</h3>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(['건축', '교통·운송', '기계·금속', '산업', '소재·재료', '전기·전자', '정밀·에너지', '컴퓨터·통신', '토목·도시', '화공', '기타'])

with tab1:
    if len(p1_titlelist1) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p1_titlelist1[-1]:
            with st.expander(p1_titlelist1[-1]):
                st.write(p1_textlist1[-1])

                if p1_encodedimagelist1 and p1_encodedimagelist1[-1]:
                    decoded_image1 = base64.b64decode(p1_encodedimagelist1[-1])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p1_titlelist1) >= 2 and p1_titlelist1[-2]:
            with st.expander(p1_titlelist1[-2]):
                st.write(p1_textlist1[-2])

                if p1_encodedimagelist1 and p1_encodedimagelist1[-2]:
                    decoded_image1 = base64.b64decode(p1_encodedimagelist1[-2])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p1_titlelist1) >= 3 and p1_titlelist1[-3]:
            with st.expander(p1_titlelist1[-3]):
                st.write(p1_textlist1[-3])

                if p1_encodedimagelist1 and p1_encodedimagelist1[-3]:
                    decoded_image1 = base64.b64decode(p1_encodedimagelist1[-3])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p1_titlelist1) >= 4 and p1_titlelist1[-4]:
            with st.expander(p1_titlelist1[-4]):
                st.write(p1_textlist1[-4])

                if p1_encodedimagelist1 and p1_encodedimagelist1[-4]:
                    decoded_image1 = base64.b64decode(p1_encodedimagelist1[-4])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p1_titlelist1) >= 5 and p1_titlelist1[-5]:
            with st.expander(p1_titlelist1[-5]):
                st.write(p1_textlist1[-5])

                if p1_encodedimagelist1 and p1_encodedimagelist1[-5]:
                    decoded_image1 = base64.b64decode(p1_encodedimagelist1[-5])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p1_titlelist1) >= 6 and p1_titlelist1[-6]:
            with st.expander(p1_titlelist1[-6]):
                st.write(p1_textlist1[-6])

                if p1_encodedimagelist1 and p1_encodedimagelist1[-6]:
                    decoded_image1 = base64.b64decode(p1_encodedimagelist1[-6])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p1_titlelist1) >= 7 and p1_titlelist1[-7]:
            with st.expander(p1_titlelist1[-7]):
                st.write(p1_textlist1[-7])

                if p1_encodedimagelist1 and p1_encodedimagelist1[-7]:
                    decoded_image1 = base64.b64decode(p1_encodedimagelist1[-7])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p1_titlelist1) >= 8 and p1_titlelist1[-8]:
            with st.expander(p1_titlelist1[-8]):
                st.write(p1_textlist1[-8])

                if p1_encodedimagelist1 and p1_encodedimagelist1[-8]:
                    decoded_image1 = base64.b64decode(p1_encodedimagelist1[-8])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p1_titlelist1) >= 9 and p1_titlelist1[-9]:
            with st.expander(p1_titlelist1[-9]):
                st.write(p1_textlist1[-9])

                if p1_encodedimagelist1 and p1_encodedimagelist1[-9]:
                    decoded_image1 = base64.b64decode(p1_encodedimagelist1[-9])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p1_titlelist1) >= 10 and p1_titlelist1[-10]:
            with st.expander(p1_titlelist1[-10]):
                st.write(p1_textlist1[-10])

                if p1_encodedimagelist1 and p1_encodedimagelist1[-10]:
                    decoded_image1 = base64.b64decode(p1_encodedimagelist1[-10])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

with tab2:
    if len(p1_titlelist2) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p1_titlelist2[-1]:
            with st.expander(p1_titlelist2[-1]):
                st.write(p1_textlist2[-1])

                if p1_encodedimagelist2 and p1_encodedimagelist2[-1]:
                    decoded_image2 = base64.b64decode(p1_encodedimagelist2[-1])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p1_titlelist2) >= 2 and p1_titlelist2[-2]:
            with st.expander(p1_titlelist2[-2]):
                st.write(p1_textlist2[-2])

                if p1_encodedimagelist2 and p1_encodedimagelist2[-2]:
                    decoded_image2 = base64.b64decode(p1_encodedimagelist2[-2])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p1_titlelist2) >= 3 and p1_titlelist2[-3]:
            with st.expander(p1_titlelist2[-3]):
                st.write(p1_textlist2[-3])

                if p1_encodedimagelist2 and p1_encodedimagelist2[-3]:
                    decoded_image2 = base64.b64decode(p1_encodedimagelist2[-3])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p1_titlelist2) >= 4 and p1_titlelist2[-4]:
            with st.expander(p1_titlelist2[-4]):
                st.write(p1_textlist2[-4])

                if p1_encodedimagelist2 and p1_encodedimagelist2[-4]:
                    decoded_image2 = base64.b64decode(p1_encodedimagelist2[-4])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p1_titlelist2) >= 5 and p1_titlelist2[-5]:
            with st.expander(p1_titlelist2[-5]):
                st.write(p1_textlist2[-5])

                if p1_encodedimagelist2 and p1_encodedimagelist2[-5]:
                    decoded_image2 = base64.b64decode(p1_encodedimagelist2[-5])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p1_titlelist2) >= 6 and p1_titlelist2[-6]:
            with st.expander(p1_titlelist2[-6]):
                st.write(p1_textlist2[-6])

                if p1_encodedimagelist2 and p1_encodedimagelist2[-6]:
                    decoded_image2 = base64.b64decode(p1_encodedimagelist2[-6])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p1_titlelist2) >= 7 and p1_titlelist2[-7]:
            with st.expander(p1_titlelist2[-7]):
                st.write(p1_textlist2[-7])

                if p1_encodedimagelist2 and p1_encodedimagelist2[-7]:
                    decoded_image2 = base64.b64decode(p1_encodedimagelist2[-7])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p1_titlelist2) >= 8 and p1_titlelist2[-8]:
            with st.expander(p1_titlelist2[-8]):
                st.write(p1_textlist2[-8])

                if p1_encodedimagelist2 and p1_encodedimagelist2[-8]:
                    decoded_image2 = base64.b64decode(p1_encodedimagelist2[-8])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p1_titlelist2) >= 9 and p1_titlelist2[-9]:
            with st.expander(p1_titlelist2[-9]):
                st.write(p1_textlist2[-9])

                if p1_encodedimagelist2 and p1_encodedimagelist2[-9]:
                    decoded_image2 = base64.b64decode(p1_encodedimagelist2[-9])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p1_titlelist2) >= 10 and p1_titlelist2[-10]:
            with st.expander(p1_titlelist2[-10]):
                st.write(p1_textlist2[-10])

                if p1_encodedimagelist2 and p1_encodedimagelist2[-10]:
                    decoded_image2 = base64.b64decode(p1_encodedimagelist2[-10])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

with tab3:
    if len(p1_titlelist3) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p1_titlelist3[-1]:
            with st.expander(p1_titlelist3[-1]):
                st.write(p1_textlist3[-1])

                if p1_encodedimagelist3 and p1_encodedimagelist3[-1]:
                    decoded_image3 = base64.b64decode(p1_encodedimagelist3[-1])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p1_titlelist3) >= 2 and p1_titlelist3[-2]:
            with st.expander(p1_titlelist3[-2]):
                st.write(p1_textlist3[-2])

                if p1_encodedimagelist3 and p1_encodedimagelist3[-2]:
                    decoded_image3 = base64.b64decode(p1_encodedimagelist3[-2])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p1_titlelist3) >= 3 and p1_titlelist3[-3]:
            with st.expander(p1_titlelist3[-3]):
                st.write(p1_textlist3[-3])

                if p1_encodedimagelist3 and p1_encodedimagelist3[-3]:
                    decoded_image3 = base64.b64decode(p1_encodedimagelist3[-3])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p1_titlelist3) >= 4 and p1_titlelist3[-4]:
            with st.expander(p1_titlelist3[-4]):
                st.write(p1_textlist3[-4])

                if p1_encodedimagelist3 and p1_encodedimagelist3[-4]:
                    decoded_image3 = base64.b64decode(p1_encodedimagelist3[-4])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p1_titlelist3) >= 5 and p1_titlelist3[-5]:
            with st.expander(p1_titlelist3[-5]):
                st.write(p1_textlist3[-5])

                if p1_encodedimagelist3 and p1_encodedimagelist3[-5]:
                    decoded_image3 = base64.b64decode(p1_encodedimagelist3[-5])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p1_titlelist3) >= 6 and p1_titlelist3[-6]:
            with st.expander(p1_titlelist3[-6]):
                st.write(p1_textlist3[-6])

                if p1_encodedimagelist3 and p1_encodedimagelist3[-6]:
                    decoded_image3 = base64.b64decode(p1_encodedimagelist3[-6])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p1_titlelist3) >= 7 and p1_titlelist3[-7]:
            with st.expander(p1_titlelist3[-7]):
                st.write(p1_textlist3[-7])

                if p1_encodedimagelist3 and p1_encodedimagelist3[-7]:
                    decoded_image3 = base64.b64decode(p1_encodedimagelist3[-7])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p1_titlelist3) >= 8 and p1_titlelist3[-8]:
            with st.expander(p1_titlelist3[-8]):
                st.write(p1_textlist3[-8])

                if p1_encodedimagelist3 and p1_encodedimagelist3[-8]:
                    decoded_image3 = base64.b64decode(p1_encodedimagelist3[-8])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p1_titlelist3) >= 9 and p1_titlelist3[-9]:
            with st.expander(p1_titlelist3[-9]):
                st.write(p1_textlist3[-9])

                if p1_encodedimagelist3 and p1_encodedimagelist3[-9]:
                    decoded_image3 = base64.b64decode(p1_encodedimagelist3[-9])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p1_titlelist3) >= 10 and p1_titlelist3[-10]:
            with st.expander(p1_titlelist3[-10]):
                st.write(p1_textlist3[-10])

                if p1_encodedimagelist3 and p1_encodedimagelist3[-10]:
                    decoded_image3 = base64.b64decode(p1_encodedimagelist3[-10])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

with tab4:
    if len(p1_titlelist4) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p1_titlelist4[-1]:
            with st.expander(p1_titlelist4[-1]):
                st.write(p1_textlist4[-1])

                if p1_encodedimagelist4 and p1_encodedimagelist4[-1]:
                    decoded_image4 = base64.b64decode(p1_encodedimagelist4[-1])
                    display_image4 = Image.open(BytesIO(decoded_image4))
                    st.image(display_image4)

        if len(p1_titlelist4) >= 2 and p1_titlelist4[-2]:
            with st.expander(p1_titlelist4[-2]):
                st.write(p1_textlist4[-2])

                if p1_encodedimagelist4 and p1_encodedimagelist4[-2]:
                    decoded_image4 = base64.b64decode(p1_encodedimagelist4[-2])
                    display_image4 = Image.open(BytesIO(decoded_image4))
                    st.image(display_image4)

        if len(p1_titlelist4) >= 3 and p1_titlelist4[-3]:
            with st.expander(p1_titlelist4[-3]):
                st.write(p1_textlist4[-3])

                if p1_encodedimagelist4 and p1_encodedimagelist4[-3]:
                    decoded_image4 = base64.b64decode(p1_encodedimagelist4[-3])
                    display_image4 = Image.open(BytesIO(decoded_image4))
                    st.image(display_image4)

        if len(p1_titlelist4) >= 4 and p1_titlelist4[-4]:
            with st.expander(p1_titlelist4[-4]):
                st.write(p1_textlist4[-4])

                if p1_encodedimagelist4 and p1_encodedimagelist4[-4]:
                    decoded_image4 = base64.b64decode(p1_encodedimagelist4[-4])
                    display_image4 = Image.open(BytesIO(decoded_image4))
                    st.image(display_image4)

        if len(p1_titlelist4) >= 5 and p1_titlelist4[-5]:
            with st.expander(p1_titlelist4[-5]):
                st.write(p1_textlist4[-5])

                if p1_encodedimagelist4 and p1_encodedimagelist4[-5]:
                    decoded_image4 = base64.b64decode(p1_encodedimagelist4[-5])
                    display_image4 = Image.open(BytesIO(decoded_image4))
                    st.image(display_image4)

        if len(p1_titlelist4) >= 6 and p1_titlelist4[-6]:
            with st.expander(p1_titlelist4[-6]):
                st.write(p1_textlist4[-6])

                if p1_encodedimagelist4 and p1_encodedimagelist4[-6]:
                    decoded_image4 = base64.b64decode(p1_encodedimagelist4[-6])
                    display_image4 = Image.open(BytesIO(decoded_image4))
                    st.image(display_image4)

        if len(p1_titlelist4) >= 7 and p1_titlelist4[-7]:
            with st.expander(p1_titlelist4[-7]):
                st.write(p1_textlist4[-7])

                if p1_encodedimagelist4 and p1_encodedimagelist4[-7]:
                    decoded_image4 = base64.b64decode(p1_encodedimagelist4[-7])
                    display_image4 = Image.open(BytesIO(decoded_image4))
                    st.image(display_image4)

        if len(p1_titlelist4) >= 8 and p1_titlelist4[-8]:
            with st.expander(p1_titlelist4[-8]):
                st.write(p1_textlist4[-8])

                if p1_encodedimagelist4 and p1_encodedimagelist4[-8]:
                    decoded_image4 = base64.b64decode(p1_encodedimagelist4[-8])
                    display_image4 = Image.open(BytesIO(decoded_image4))
                    st.image(display_image4)

        if len(p1_titlelist4) >= 9 and p1_titlelist4[-9]:
            with st.expander(p1_titlelist4[-9]):
                st.write(p1_textlist4[-9])

                if p1_encodedimagelist4 and p1_encodedimagelist4[-9]:
                    decoded_image4 = base64.b64decode(p1_encodedimagelist4[-9])
                    display_image4 = Image.open(BytesIO(decoded_image4))
                    st.image(display_image4)

        if len(p1_titlelist4) >= 10 and p1_titlelist4[-10]:
            with st.expander(p1_titlelist4[-10]):
                st.write(p1_textlist4[-10])

                if p1_encodedimagelist4 and p1_encodedimagelist4[-10]:
                    decoded_image4 = base64.b64decode(p1_encodedimagelist4[-10])
                    display_image4 = Image.open(BytesIO(decoded_image4))
                    st.image(display_image4)

with tab5:
    if len(p1_titlelist5) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p1_titlelist5[-1]:
            with st.expander(p1_titlelist5[-1]):
                st.write(p1_textlist5[-1])

                if p1_encodedimagelist5 and p1_encodedimagelist5[-1]:
                    decoded_image5 = base64.b64decode(p1_encodedimagelist5[-1])
                    display_image5 = Image.open(BytesIO(decoded_image5))
                    st.image(display_image5)

        if len(p1_titlelist5) >= 2 and p1_titlelist5[-2]:
            with st.expander(p1_titlelist5[-2]):
                st.write(p1_textlist5[-2])

                if p1_encodedimagelist5 and p1_encodedimagelist5[-2]:
                    decoded_image5 = base64.b64decode(p1_encodedimagelist5[-2])
                    display_image5 = Image.open(BytesIO(decoded_image5))
                    st.image(display_image5)

        if len(p1_titlelist5) >= 3 and p1_titlelist5[-3]:
            with st.expander(p1_titlelist5[-3]):
                st.write(p1_textlist5[-3])

                if p1_encodedimagelist5 and p1_encodedimagelist5[-3]:
                    decoded_image5 = base64.b64decode(p1_encodedimagelist5[-3])
                    display_image5 = Image.open(BytesIO(decoded_image5))
                    st.image(display_image5)

        if len(p1_titlelist5) >= 4 and p1_titlelist5[-4]:
            with st.expander(p1_titlelist5[-4]):
                st.write(p1_textlist5[-4])

                if p1_encodedimagelist5 and p1_encodedimagelist5[-4]:
                    decoded_image5 = base64.b64decode(p1_encodedimagelist5[-4])
                    display_image5 = Image.open(BytesIO(decoded_image5))
                    st.image(display_image5)

        if len(p1_titlelist5) >= 5 and p1_titlelist5[-5]:
            with st.expander(p1_titlelist5[-5]):
                st.write(p1_textlist5[-5])

                if p1_encodedimagelist5 and p1_encodedimagelist5[-5]:
                    decoded_image5 = base64.b64decode(p1_encodedimagelist5[-5])
                    display_image5 = Image.open(BytesIO(decoded_image5))
                    st.image(display_image5)

        if len(p1_titlelist5) >= 6 and p1_titlelist5[-6]:
            with st.expander(p1_titlelist5[-6]):
                st.write(p1_textlist5[-6])

                if p1_encodedimagelist5 and p1_encodedimagelist5[-6]:
                    decoded_image5 = base64.b64decode(p1_encodedimagelist5[-6])
                    display_image5 = Image.open(BytesIO(decoded_image5))
                    st.image(display_image5)

        if len(p1_titlelist5) >= 7 and p1_titlelist5[-7]:
            with st.expander(p1_titlelist5[-7]):
                st.write(p1_textlist5[-7])

                if p1_encodedimagelist5 and p1_encodedimagelist5[-7]:
                    decoded_image5 = base64.b64decode(p1_encodedimagelist5[-7])
                    display_image5 = Image.open(BytesIO(decoded_image5))
                    st.image(display_image5)

        if len(p1_titlelist5) >= 8 and p1_titlelist5[-8]:
            with st.expander(p1_titlelist5[-8]):
                st.write(p1_textlist5[-8])

                if p1_encodedimagelist5 and p1_encodedimagelist5[-8]:
                    decoded_image5 = base64.b64decode(p1_encodedimagelist5[-8])
                    display_image5 = Image.open(BytesIO(decoded_image5))
                    st.image(display_image5)

        if len(p1_titlelist5) >= 9 and p1_titlelist5[-9]:
            with st.expander(p1_titlelist5[-9]):
                st.write(p1_textlist5[-9])

                if p1_encodedimagelist5 and p1_encodedimagelist5[-9]:
                    decoded_image5 = base64.b64decode(p1_encodedimagelist5[-9])
                    display_image5 = Image.open(BytesIO(decoded_image5))
                    st.image(display_image5)

        if len(p1_titlelist5) >= 10 and p1_titlelist5[-10]:
            with st.expander(p1_titlelist5[-10]):
                st.write(p1_textlist5[-10])

                if p1_encodedimagelist5 and p1_encodedimagelist5[-10]:
                    decoded_image5 = base64.b64decode(p1_encodedimagelist5[-10])
                    display_image5 = Image.open(BytesIO(decoded_image5))
                    st.image(display_image5)

with tab6:
    if len(p1_titlelist6) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p1_titlelist6[-1]:
            with st.expander(p1_titlelist6[-1]):
                st.write(p1_textlist6[-1])

                if p1_encodedimagelist6 and p1_encodedimagelist6[-1]:
                    decoded_image6 = base64.b64decode(p1_encodedimagelist6[-1])
                    display_image6 = Image.open(BytesIO(decoded_image6))
                    st.image(display_image6)

        if len(p1_titlelist6) >= 2 and p1_titlelist6[-2]:
            with st.expander(p1_titlelist6[-2]):
                st.write(p1_textlist6[-2])

                if p1_encodedimagelist6 and p1_encodedimagelist6[-2]:
                    decoded_image6 = base64.b64decode(p1_encodedimagelist6[-2])
                    display_image6 = Image.open(BytesIO(decoded_image6))
                    st.image(display_image6)

        if len(p1_titlelist6) >= 3 and p1_titlelist6[-3]:
            with st.expander(p1_titlelist6[-3]):
                st.write(p1_textlist6[-3])

                if p1_encodedimagelist6 and p1_encodedimagelist6[-3]:
                    decoded_image6 = base64.b64decode(p1_encodedimagelist6[-3])
                    display_image6 = Image.open(BytesIO(decoded_image6))
                    st.image(display_image6)

        if len(p1_titlelist6) >= 4 and p1_titlelist6[-4]:
            with st.expander(p1_titlelist6[-4]):
                st.write(p1_textlist6[-4])

                if p1_encodedimagelist6 and p1_encodedimagelist6[-4]:
                    decoded_image6 = base64.b64decode(p1_encodedimagelist6[-4])
                    display_image6 = Image.open(BytesIO(decoded_image6))
                    st.image(display_image6)

        if len(p1_titlelist6) >= 5 and p1_titlelist6[-5]:
            with st.expander(p1_titlelist6[-5]):
                st.write(p1_textlist6[-5])

                if p1_encodedimagelist6 and p1_encodedimagelist6[-5]:
                    decoded_image6 = base64.b64decode(p1_encodedimagelist6[-5])
                    display_image6 = Image.open(BytesIO(decoded_image6))
                    st.image(display_image6)

        if len(p1_titlelist6) >= 6 and p1_titlelist6[-6]:
            with st.expander(p1_titlelist6[-6]):
                st.write(p1_textlist6[-6])

                if p1_encodedimagelist6 and p1_encodedimagelist6[-6]:
                    decoded_image6 = base64.b64decode(p1_encodedimagelist6[-6])
                    display_image6 = Image.open(BytesIO(decoded_image6))
                    st.image(display_image6)

        if len(p1_titlelist6) >= 7 and p1_titlelist6[-7]:
            with st.expander(p1_titlelist6[-7]):
                st.write(p1_textlist6[-7])

                if p1_encodedimagelist6 and p1_encodedimagelist6[-7]:
                    decoded_image6 = base64.b64decode(p1_encodedimagelist6[-7])
                    display_image6 = Image.open(BytesIO(decoded_image6))
                    st.image(display_image6)

        if len(p1_titlelist6) >= 8 and p1_titlelist6[-8]:
            with st.expander(p1_titlelist6[-8]):
                st.write(p1_textlist6[-8])

                if p1_encodedimagelist6 and p1_encodedimagelist6[-8]:
                    decoded_image6 = base64.b64decode(p1_encodedimagelist6[-8])
                    display_image6 = Image.open(BytesIO(decoded_image6))
                    st.image(display_image6)

        if len(p1_titlelist6) >= 9 and p1_titlelist6[-9]:
            with st.expander(p1_titlelist6[-9]):
                st.write(p1_textlist6[-9])

                if p1_encodedimagelist6 and p1_encodedimagelist6[-9]:
                    decoded_image6 = base64.b64decode(p1_encodedimagelist6[-9])
                    display_image6 = Image.open(BytesIO(decoded_image6))
                    st.image(display_image6)

        if len(p1_titlelist6) >= 10 and p1_titlelist6[-10]:
            with st.expander(p1_titlelist6[-10]):
                st.write(p1_textlist6[-10])

                if p1_encodedimagelist6 and p1_encodedimagelist6[-10]:
                    decoded_image6 = base64.b64decode(p1_encodedimagelist6[-10])
                    display_image6 = Image.open(BytesIO(decoded_image6))
                    st.image(display_image6)

with tab7:
    if len(p1_titlelist7) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p1_titlelist7[-1]:
            with st.expander(p1_titlelist7[-1]):
                st.write(p1_textlist7[-1])

                if p1_encodedimagelist7 and p1_encodedimagelist7[-1]:
                    decoded_image7 = base64.b64decode(p1_encodedimagelist7[-1])
                    display_image7 = Image.open(BytesIO(decoded_image7))
                    st.image(display_image7)

        if len(p1_titlelist7) >= 2 and p1_titlelist7[-2]:
            with st.expander(p1_titlelist7[-2]):
                st.write(p1_textlist7[-2])

                if p1_encodedimagelist7 and p1_encodedimagelist7[-2]:
                    decoded_image7 = base64.b64decode(p1_encodedimagelist7[-2])
                    display_image7 = Image.open(BytesIO(decoded_image7))
                    st.image(display_image7)

        if len(p1_titlelist7) >= 3 and p1_titlelist7[-3]:
            with st.expander(p1_titlelist7[-3]):
                st.write(p1_textlist7[-3])

                if p1_encodedimagelist7 and p1_encodedimagelist7[-3]:
                    decoded_image7 = base64.b64decode(p1_encodedimagelist7[-3])
                    display_image7 = Image.open(BytesIO(decoded_image7))
                    st.image(display_image7)

        if len(p1_titlelist7) >= 4 and p1_titlelist7[-4]:
            with st.expander(p1_titlelist7[-4]):
                st.write(p1_textlist7[-4])

                if p1_encodedimagelist7 and p1_encodedimagelist7[-4]:
                    decoded_image7 = base64.b64decode(p1_encodedimagelist7[-4])
                    display_image7 = Image.open(BytesIO(decoded_image7))
                    st.image(display_image7)

        if len(p1_titlelist7) >= 5 and p1_titlelist7[-5]:
            with st.expander(p1_titlelist7[-5]):
                st.write(p1_textlist7[-5])

                if p1_encodedimagelist7 and p1_encodedimagelist7[-5]:
                    decoded_image7 = base64.b64decode(p1_encodedimagelist7[-5])
                    display_image7 = Image.open(BytesIO(decoded_image7))
                    st.image(display_image7)

        if len(p1_titlelist7) >= 6 and p1_titlelist7[-6]:
            with st.expander(p1_titlelist7[-6]):
                st.write(p1_textlist7[-6])

                if p1_encodedimagelist7 and p1_encodedimagelist7[-6]:
                    decoded_image7 = base64.b64decode(p1_encodedimagelist7[-6])
                    display_image7 = Image.open(BytesIO(decoded_image7))
                    st.image(display_image7)

        if len(p1_titlelist7) >= 7 and p1_titlelist7[-7]:
            with st.expander(p1_titlelist7[-7]):
                st.write(p1_textlist7[-7])

                if p1_encodedimagelist7 and p1_encodedimagelist7[-7]:
                    decoded_image7 = base64.b64decode(p1_encodedimagelist7[-7])
                    display_image7 = Image.open(BytesIO(decoded_image7))
                    st.image(display_image7)

        if len(p1_titlelist7) >= 8 and p1_titlelist7[-8]:
            with st.expander(p1_titlelist7[-8]):
                st.write(p1_textlist7[-8])

                if p1_encodedimagelist7 and p1_encodedimagelist7[-8]:
                    decoded_image7 = base64.b64decode(p1_encodedimagelist7[-8])
                    display_image7 = Image.open(BytesIO(decoded_image7))
                    st.image(display_image7)

        if len(p1_titlelist7) >= 9 and p1_titlelist7[-9]:
            with st.expander(p1_titlelist7[-9]):
                st.write(p1_textlist7[-9])

                if p1_encodedimagelist7 and p1_encodedimagelist7[-9]:
                    decoded_image7 = base64.b64decode(p1_encodedimagelist7[-9])
                    display_image7 = Image.open(BytesIO(decoded_image7))
                    st.image(display_image7)

        if len(p1_titlelist7) >= 10 and p1_titlelist7[-10]:
            with st.expander(p1_titlelist7[-10]):
                st.write(p1_textlist7[-10])

                if p1_encodedimagelist7 and p1_encodedimagelist7[-10]:
                    decoded_image7 = base64.b64decode(p1_encodedimagelist7[-10])
                    display_image7 = Image.open(BytesIO(decoded_image7))
                    st.image(display_image7)

with tab8:
    if len(p1_titlelist8) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p1_titlelist8[-1]:
            with st.expander(p1_titlelist8[-1]):
                st.write(p1_textlist8[-1])

                if p1_encodedimagelist8 and p1_encodedimagelist8[-1]:
                    decoded_image8 = base64.b64decode(p1_encodedimagelist8[-1])
                    display_image8 = Image.open(BytesIO(decoded_image8))
                    st.image(display_image8)

        if len(p1_titlelist8) >= 2 and p1_titlelist8[-2]:
            with st.expander(p1_titlelist8[-2]):
                st.write(p1_textlist8[-2])

                if p1_encodedimagelist8 and p1_encodedimagelist8[-2]:
                    decoded_image8 = base64.b64decode(p1_encodedimagelist8[-2])
                    display_image8 = Image.open(BytesIO(decoded_image8))
                    st.image(display_image8)

        if len(p1_titlelist8) >= 3 and p1_titlelist8[-3]:
            with st.expander(p1_titlelist8[-3]):
                st.write(p1_textlist8[-3])

                if p1_encodedimagelist8 and p1_encodedimagelist8[-3]:
                    decoded_image8 = base64.b64decode(p1_encodedimagelist8[-3])
                    display_image8 = Image.open(BytesIO(decoded_image8))
                    st.image(display_image8)

        if len(p1_titlelist8) >= 4 and p1_titlelist8[-4]:
            with st.expander(p1_titlelist8[-4]):
                st.write(p1_textlist8[-4])

                if p1_encodedimagelist8 and p1_encodedimagelist8[-4]:
                    decoded_image8 = base64.b64decode(p1_encodedimagelist8[-4])
                    display_image8 = Image.open(BytesIO(decoded_image8))
                    st.image(display_image8)

        if len(p1_titlelist8) >= 5 and p1_titlelist8[-5]:
            with st.expander(p1_titlelist8[-5]):
                st.write(p1_textlist8[-5])

                if p1_encodedimagelist8 and p1_encodedimagelist8[-5]:
                    decoded_image8 = base64.b64decode(p1_encodedimagelist8[-5])
                    display_image8 = Image.open(BytesIO(decoded_image8))
                    st.image(display_image8)

        if len(p1_titlelist8) >= 6 and p1_titlelist8[-6]:
            with st.expander(p1_titlelist8[-6]):
                st.write(p1_textlist8[-6])

                if p1_encodedimagelist8 and p1_encodedimagelist8[-6]:
                    decoded_image8 = base64.b64decode(p1_encodedimagelist8[-6])
                    display_image8 = Image.open(BytesIO(decoded_image8))
                    st.image(display_image8)

        if len(p1_titlelist8) >= 7 and p1_titlelist8[-7]:
            with st.expander(p1_titlelist8[-7]):
                st.write(p1_textlist8[-7])

                if p1_encodedimagelist8 and p1_encodedimagelist8[-7]:
                    decoded_image8 = base64.b64decode(p1_encodedimagelist8[-7])
                    display_image8 = Image.open(BytesIO(decoded_image8))
                    st.image(display_image8)

        if len(p1_titlelist8) >= 8 and p1_titlelist8[-8]:
            with st.expander(p1_titlelist8[-8]):
                st.write(p1_textlist8[-8])

                if p1_encodedimagelist8 and p1_encodedimagelist8[-8]:
                    decoded_image8 = base64.b64decode(p1_encodedimagelist8[-8])
                    display_image8 = Image.open(BytesIO(decoded_image8))
                    st.image(display_image8)

        if len(p1_titlelist8) >= 9 and p1_titlelist8[-9]:
            with st.expander(p1_titlelist8[-9]):
                st.write(p1_textlist8[-9])

                if p1_encodedimagelist8 and p1_encodedimagelist8[-9]:
                    decoded_image8 = base64.b64decode(p1_encodedimagelist8[-9])
                    display_image8 = Image.open(BytesIO(decoded_image8))
                    st.image(display_image8)

        if len(p1_titlelist8) >= 10 and p1_titlelist8[-10]:
            with st.expander(p1_titlelist8[-10]):
                st.write(p1_textlist8[-10])

                if p1_encodedimagelist8 and p1_encodedimagelist8[-10]:
                    decoded_image8 = base64.b64decode(p1_encodedimagelist8[-10])
                    display_image8 = Image.open(BytesIO(decoded_image8))
                    st.image(display_image8)

with tab9:
    if len(p1_titlelist9) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p1_titlelist9[-1]:
            with st.expander(p1_titlelist9[-1]):
                st.write(p1_textlist9[-1])

                if p1_encodedimagelist9 and p1_encodedimagelist9[-1]:
                    decoded_image9 = base64.b64decode(p1_encodedimagelist9[-1])
                    display_image9 = Image.open(BytesIO(decoded_image9))
                    st.image(display_image9)

        if len(p1_titlelist9) >= 2 and p1_titlelist9[-2]:
            with st.expander(p1_titlelist9[-2]):
                st.write(p1_textlist9[-2])

                if p1_encodedimagelist9 and p1_encodedimagelist9[-2]:
                    decoded_image9 = base64.b64decode(p1_encodedimagelist9[-2])
                    display_image9 = Image.open(BytesIO(decoded_image9))
                    st.image(display_image9)

        if len(p1_titlelist9) >= 3 and p1_titlelist9[-3]:
            with st.expander(p1_titlelist9[-3]):
                st.write(p1_textlist9[-3])

                if p1_encodedimagelist9 and p1_encodedimagelist9[-3]:
                    decoded_image9 = base64.b64decode(p1_encodedimagelist9[-3])
                    display_image9 = Image.open(BytesIO(decoded_image9))
                    st.image(display_image9)

        if len(p1_titlelist9) >= 4 and p1_titlelist9[-4]:
            with st.expander(p1_titlelist9[-4]):
                st.write(p1_textlist9[-4])

                if p1_encodedimagelist9 and p1_encodedimagelist9[-4]:
                    decoded_image9 = base64.b64decode(p1_encodedimagelist9[-4])
                    display_image9 = Image.open(BytesIO(decoded_image9))
                    st.image(display_image9)

        if len(p1_titlelist9) >= 5 and p1_titlelist9[-5]:
            with st.expander(p1_titlelist9[-5]):
                st.write(p1_textlist9[-5])

                if p1_encodedimagelist9 and p1_encodedimagelist9[-5]:
                    decoded_image9 = base64.b64decode(p1_encodedimagelist9[-5])
                    display_image9 = Image.open(BytesIO(decoded_image9))
                    st.image(display_image9)

        if len(p1_titlelist9) >= 6 and p1_titlelist9[-6]:
            with st.expander(p1_titlelist9[-6]):
                st.write(p1_textlist9[-6])

                if p1_encodedimagelist9 and p1_encodedimagelist9[-6]:
                    decoded_image9 = base64.b64decode(p1_encodedimagelist9[-6])
                    display_image9 = Image.open(BytesIO(decoded_image9))
                    st.image(display_image9)

        if len(p1_titlelist9) >= 7 and p1_titlelist9[-7]:
            with st.expander(p1_titlelist9[-7]):
                st.write(p1_textlist9[-7])

                if p1_encodedimagelist9 and p1_encodedimagelist9[-7]:
                    decoded_image9 = base64.b64decode(p1_encodedimagelist9[-7])
                    display_image9 = Image.open(BytesIO(decoded_image9))
                    st.image(display_image9)

        if len(p1_titlelist9) >= 8 and p1_titlelist9[-8]:
            with st.expander(p1_titlelist9[-8]):
                st.write(p1_textlist9[-8])

                if p1_encodedimagelist9 and p1_encodedimagelist9[-8]:
                    decoded_image9 = base64.b64decode(p1_encodedimagelist9[-8])
                    display_image9 = Image.open(BytesIO(decoded_image9))
                    st.image(display_image9)

        if len(p1_titlelist9) >= 9 and p1_titlelist9[-9]:
            with st.expander(p1_titlelist9[-9]):
                st.write(p1_textlist9[-9])

                if p1_encodedimagelist9 and p1_encodedimagelist9[-9]:
                    decoded_image9 = base64.b64decode(p1_encodedimagelist9[-9])
                    display_image9 = Image.open(BytesIO(decoded_image9))
                    st.image(display_image9)

        if len(p1_titlelist9) >= 10 and p1_titlelist9[-10]:
            with st.expander(p1_titlelist9[-10]):
                st.write(p1_textlist9[-10])

                if p1_encodedimagelist9 and p1_encodedimagelist9[-10]:
                    decoded_image9 = base64.b64decode(p1_encodedimagelist9[-10])
                    display_image9 = Image.open(BytesIO(decoded_image9))
                    st.image(display_image9)

with tab10:
    if len(p1_titlelist10) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p1_titlelist10[-1]:
            with st.expander(p1_titlelist10[-1]):
                st.write(p1_textlist10[-1])

                if p1_encodedimagelist10 and p1_encodedimagelist10[-1]:
                    decoded_image10 = base64.b64decode(p1_encodedimagelist10[-1])
                    display_image10 = Image.open(BytesIO(decoded_image10))
                    st.image(display_image10)

        if len(p1_titlelist10) >= 2 and p1_titlelist10[-2]:
            with st.expander(p1_titlelist10[-2]):
                st.write(p1_textlist10[-2])

                if p1_encodedimagelist10 and p1_encodedimagelist10[-2]:
                    decoded_image10 = base64.b64decode(p1_encodedimagelist10[-2])
                    display_image10 = Image.open(BytesIO(decoded_image10))
                    st.image(display_image10)

        if len(p1_titlelist10) >= 3 and p1_titlelist10[-3]:
            with st.expander(p1_titlelist10[-3]):
                st.write(p1_textlist10[-3])

                if p1_encodedimagelist10 and p1_encodedimagelist10[-3]:
                    decoded_image10 = base64.b64decode(p1_encodedimagelist10[-3])
                    display_image10 = Image.open(BytesIO(decoded_image10))
                    st.image(display_image10)

        if len(p1_titlelist10) >= 4 and p1_titlelist10[-4]:
            with st.expander(p1_titlelist10[-4]):
                st.write(p1_textlist10[-4])

                if p1_encodedimagelist10 and p1_encodedimagelist10[-4]:
                    decoded_image10 = base64.b64decode(p1_encodedimagelist10[-4])
                    display_image10 = Image.open(BytesIO(decoded_image10))
                    st.image(display_image10)

        if len(p1_titlelist10) >= 5 and p1_titlelist10[-5]:
            with st.expander(p1_titlelist10[-5]):
                st.write(p1_textlist10[-5])

                if p1_encodedimagelist10 and p1_encodedimagelist10[-5]:
                    decoded_image10 = base64.b64decode(p1_encodedimagelist10[-5])
                    display_image10 = Image.open(BytesIO(decoded_image10))
                    st.image(display_image10)

        if len(p1_titlelist10) >= 6 and p1_titlelist10[-6]:
            with st.expander(p1_titlelist10[-6]):
                st.write(p1_textlist10[-6])

                if p1_encodedimagelist10 and p1_encodedimagelist10[-6]:
                    decoded_image10 = base64.b64decode(p1_encodedimagelist10[-6])
                    display_image10 = Image.open(BytesIO(decoded_image10))
                    st.image(display_image10)

        if len(p1_titlelist10) >= 7 and p1_titlelist10[-7]:
            with st.expander(p1_titlelist10[-7]):
                st.write(p1_textlist10[-7])

                if p1_encodedimagelist10 and p1_encodedimagelist10[-7]:
                    decoded_image10 = base64.b64decode(p1_encodedimagelist10[-7])
                    display_image10 = Image.open(BytesIO(decoded_image10))
                    st.image(display_image10)

        if len(p1_titlelist10) >= 8 and p1_titlelist10[-8]:
            with st.expander(p1_titlelist10[-8]):
                st.write(p1_textlist10[-8])

                if p1_encodedimagelist10 and p1_encodedimagelist10[-8]:
                    decoded_image10 = base64.b64decode(p1_encodedimagelist10[-8])
                    display_image10 = Image.open(BytesIO(decoded_image10))
                    st.image(display_image10)

        if len(p1_titlelist10) >= 9 and p1_titlelist10[-9]:
            with st.expander(p1_titlelist10[-9]):
                st.write(p1_textlist10[-9])

                if p1_encodedimagelist10 and p1_encodedimagelist10[-9]:
                    decoded_image10 = base64.b64decode(p1_encodedimagelist10[-9])
                    display_image10 = Image.open(BytesIO(decoded_image10))
                    st.image(display_image10)

        if len(p1_titlelist10) >= 10 and p1_titlelist10[-10]:
            with st.expander(p1_titlelist10[-10]):
                st.write(p1_textlist10[-10])

                if p1_encodedimagelist10 and p1_encodedimagelist10[-10]:
                    decoded_image10 = base64.b64decode(p1_encodedimagelist10[-10])
                    display_image10 = Image.open(BytesIO(decoded_image10))
                    st.image(display_image10)

with tab11:
    if len(p1_titlelist11) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p1_titlelist11[-1]:
            with st.expander(p1_titlelist11[-1]):
                st.write(p1_textlist11[-1])

                if p1_encodedimagelist11 and p1_encodedimagelist11[-1]:
                    decoded_image11 = base64.b64decode(p1_encodedimagelist11[-1])
                    display_image11 = Image.open(BytesIO(decoded_image11))
                    st.image(display_image11)

        if len(p1_titlelist11) >= 2 and p1_titlelist11[-2]:
            with st.expander(p1_titlelist11[-2]):
                st.write(p1_textlist11[-2])

                if p1_encodedimagelist11 and p1_encodedimagelist11[-2]:
                    decoded_image11 = base64.b64decode(p1_encodedimagelist11[-2])
                    display_image11 = Image.open(BytesIO(decoded_image11))
                    st.image(display_image11)

        if len(p1_titlelist11) >= 3 and p1_titlelist11[-3]:
            with st.expander(p1_titlelist11[-3]):
                st.write(p1_textlist11[-3])

                if p1_encodedimagelist11 and p1_encodedimagelist11[-3]:
                    decoded_image11 = base64.b64decode(p1_encodedimagelist11[-3])
                    display_image11 = Image.open(BytesIO(decoded_image11))
                    st.image(display_image11)

        if len(p1_titlelist11) >= 4 and p1_titlelist11[-4]:
            with st.expander(p1_titlelist11[-4]):
                st.write(p1_textlist11[-4])

                if p1_encodedimagelist11 and p1_encodedimagelist11[-4]:
                    decoded_image11 = base64.b64decode(p1_encodedimagelist11[-4])
                    display_image11 = Image.open(BytesIO(decoded_image11))
                    st.image(display_image11)

        if len(p1_titlelist11) >= 5 and p1_titlelist11[-5]:
            with st.expander(p1_titlelist11[-5]):
                st.write(p1_textlist11[-5])

                if p1_encodedimagelist11 and p1_encodedimagelist11[-5]:
                    decoded_image11 = base64.b64decode(p1_encodedimagelist11[-5])
                    display_image11 = Image.open(BytesIO(decoded_image11))
                    st.image(display_image11)

        if len(p1_titlelist11) >= 6 and p1_titlelist11[-6]:
            with st.expander(p1_titlelist11[-6]):
                st.write(p1_textlist11[-6])

                if p1_encodedimagelist11 and p1_encodedimagelist11[-6]:
                    decoded_image11 = base64.b64decode(p1_encodedimagelist11[-6])
                    display_image11 = Image.open(BytesIO(decoded_image11))
                    st.image(display_image11)

        if len(p1_titlelist11) >= 7 and p1_titlelist11[-7]:
            with st.expander(p1_titlelist11[-7]):
                st.write(p1_textlist11[-7])

                if p1_encodedimagelist11 and p1_encodedimagelist11[-7]:
                    decoded_image11 = base64.b64decode(p1_encodedimagelist11[-7])
                    display_image11 = Image.open(BytesIO(decoded_image11))
                    st.image(display_image11)

        if len(p1_titlelist11) >= 8 and p1_titlelist11[-8]:
            with st.expander(p1_titlelist11[-8]):
                st.write(p1_textlist11[-8])

                if p1_encodedimagelist11 and p1_encodedimagelist11[-8]:
                    decoded_image11 = base64.b64decode(p1_encodedimagelist11[-8])
                    display_image11 = Image.open(BytesIO(decoded_image11))
                    st.image(display_image11)

        if len(p1_titlelist11) >= 9 and p1_titlelist11[-9]:
            with st.expander(p1_titlelist11[-9]):
                st.write(p1_textlist11[-9])

                if p1_encodedimagelist11 and p1_encodedimagelist11[-9]:
                    decoded_image11 = base64.b64decode(p1_encodedimagelist11[-9])
                    display_image11 = Image.open(BytesIO(decoded_image11))
                    st.image(display_image11)

        if len(p1_titlelist11) >= 10 and p1_titlelist11[-10]:
            with st.expander(p1_titlelist11[-10]):
                st.write(p1_textlist11[-10])

                if p1_encodedimagelist11 and p1_encodedimagelist11[-10]:
                    decoded_image11 = base64.b64decode(p1_encodedimagelist11[-10])
                    display_image11 = Image.open(BytesIO(decoded_image11))
                    st.image(display_image11)

