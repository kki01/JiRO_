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

p3_list = []
p3_encodedimagelist = []
p3_titlelist1 = []
p3_textlist1 = []
p3_encodedimagelist1 = []
p3_titlelist2 = []
p3_textlist2 = []
p3_encodedimagelist2 = []
p3_titlelist3 = []
p3_textlist3 = []
p3_encodedimagelist3 = []

for row in data:
    if row[3] == "경영·경제":
        p3_titlelist1.append(row[0])
        p3_textlist1.append(row[1])
        p3_encodedimagelist1.append(row[4])

    elif row[3] == "법률":
        p3_titlelist2.append(row[0])
        p3_textlist2.append(row[1])
        p3_encodedimagelist2.append(row[4])

    elif row[3] == "사회교육":
        p3_titlelist3.append(row[0])
        p3_textlist3.append(row[1])
        p3_encodedimagelist3.append(row[4])

###########################################################################################################
# sidebar
###########################################################################################################


###########################################################################################################
# main page 
###########################################################################################################

st.markdown('<h3 style="text-align: center;">사회계열</h3>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(['경영·경제', '법률', '사회과학'])


with tab1:
    if len(p3_titlelist1) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p3_titlelist1[-1]:
            with st.expander(p3_titlelist1[-1]):
                st.write(p3_textlist1[-1])

                if p3_encodedimagelist1 and p3_encodedimagelist1[-1]:
                    decoded_image1 = base64.b64decode(p3_encodedimagelist1[-1])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p3_titlelist1) >= 2 and p3_titlelist1[-2]:
            with st.expander(p3_titlelist1[-2]):
                st.write(p3_textlist1[-2])

                if p3_encodedimagelist1 and p3_encodedimagelist1[-2]:
                    decoded_image1 = base64.b64decode(p3_encodedimagelist1[-2])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p3_titlelist1) >= 3 and p3_titlelist1[-3]:
            with st.expander(p3_titlelist1[-3]):
                st.write(p3_textlist1[-3])

                if p3_encodedimagelist1 and p3_encodedimagelist1[-3]:
                    decoded_image1 = base64.b64decode(p3_encodedimagelist1[-3])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p3_titlelist1) >= 4 and p3_titlelist1[-4]:
            with st.expander(p3_titlelist1[-4]):
                st.write(p3_textlist1[-4])

                if p3_encodedimagelist1 and p3_encodedimagelist1[-4]:
                    decoded_image1 = base64.b64decode(p3_encodedimagelist1[-4])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p3_titlelist1) >= 5 and p3_titlelist1[-5]:
            with st.expander(p3_titlelist1[-5]):
                st.write(p3_textlist1[-5])

                if p3_encodedimagelist1 and p3_encodedimagelist1[-5]:
                    decoded_image1 = base64.b64decode(p3_encodedimagelist1[-5])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p3_titlelist1) >= 6 and p3_titlelist1[-6]:
            with st.expander(p3_titlelist1[-6]):
                st.write(p3_textlist1[-6])

                if p3_encodedimagelist1 and p3_encodedimagelist1[-6]:
                    decoded_image1 = base64.b64decode(p3_encodedimagelist1[-6])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p3_titlelist1) >= 7 and p3_titlelist1[-7]:
            with st.expander(p3_titlelist1[-7]):
                st.write(p3_textlist1[-7])

                if p3_encodedimagelist1 and p3_encodedimagelist1[-7]:
                    decoded_image1 = base64.b64decode(p3_encodedimagelist1[-7])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p3_titlelist1) >= 8 and p3_titlelist1[-8]:
            with st.expander(p3_titlelist1[-8]):
                st.write(p3_textlist1[-8])

                if p3_encodedimagelist1 and p3_encodedimagelist1[-8]:
                    decoded_image1 = base64.b64decode(p3_encodedimagelist1[-8])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p3_titlelist1) >= 9 and p3_titlelist1[-9]:
            with st.expander(p3_titlelist1[-9]):
                st.write(p3_textlist1[-9])

                if p3_encodedimagelist1 and p3_encodedimagelist1[-9]:
                    decoded_image1 = base64.b64decode(p3_encodedimagelist1[-9])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

        if len(p3_titlelist1) >= 10 and p3_titlelist1[-10]:
            with st.expander(p3_titlelist1[-10]):
                st.write(p3_textlist1[-10])

                if p3_encodedimagelist1 and p3_encodedimagelist1[-10]:
                    decoded_image1 = base64.b64decode(p3_encodedimagelist1[-10])
                    display_image1 = Image.open(BytesIO(decoded_image1))
                    st.image(display_image1)

with tab2:
    if len(p3_titlelist2) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p3_titlelist2[-1]:
            with st.expander(p3_titlelist2[-1]):
                st.write(p3_textlist2[-1])

                if p3_encodedimagelist2 and p3_encodedimagelist2[-1]:
                    decoded_image2 = base64.b64decode(p3_encodedimagelist2[-1])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p3_titlelist2) >= 2 and p3_titlelist2[-2]:
            with st.expander(p3_titlelist2[-2]):
                st.write(p3_textlist2[-2])

                if p3_encodedimagelist2 and p3_encodedimagelist2[-2]:
                    decoded_image2 = base64.b64decode(p3_encodedimagelist2[-2])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p3_titlelist2) >= 3 and p3_titlelist2[-3]:
            with st.expander(p3_titlelist2[-3]):
                st.write(p3_textlist2[-3])

                if p3_encodedimagelist2 and p3_encodedimagelist2[-3]:
                    decoded_image2 = base64.b64decode(p3_encodedimagelist2[-3])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p3_titlelist2) >= 4 and p3_titlelist2[-4]:
            with st.expander(p3_titlelist2[-4]):
                st.write(p3_textlist2[-4])

                if p3_encodedimagelist2 and p3_encodedimagelist2[-4]:
                    decoded_image2 = base64.b64decode(p3_encodedimagelist2[-4])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p3_titlelist2) >= 5 and p3_titlelist2[-5]:
            with st.expander(p3_titlelist2[-5]):
                st.write(p3_textlist2[-5])

                if p3_encodedimagelist2 and p3_encodedimagelist2[-5]:
                    decoded_image2 = base64.b64decode(p3_encodedimagelist2[-5])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p3_titlelist2) >= 6 and p3_titlelist2[-6]:
            with st.expander(p3_titlelist2[-6]):
                st.write(p3_textlist2[-6])

                if p3_encodedimagelist2 and p3_encodedimagelist2[-6]:
                    decoded_image2 = base64.b64decode(p3_encodedimagelist2[-6])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p3_titlelist2) >= 7 and p3_titlelist2[-7]:
            with st.expander(p3_titlelist2[-7]):
                st.write(p3_textlist2[-7])

                if p3_encodedimagelist2 and p3_encodedimagelist2[-7]:
                    decoded_image2 = base64.b64decode(p3_encodedimagelist2[-7])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p3_titlelist2) >= 8 and p3_titlelist2[-8]:
            with st.expander(p3_titlelist2[-8]):
                st.write(p3_textlist2[-8])

                if p3_encodedimagelist2 and p3_encodedimagelist2[-8]:
                    decoded_image2 = base64.b64decode(p3_encodedimagelist2[-8])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p3_titlelist2) >= 9 and p3_titlelist2[-9]:
            with st.expander(p3_titlelist2[-9]):
                st.write(p3_textlist2[-9])

                if p3_encodedimagelist2 and p3_encodedimagelist2[-9]:
                    decoded_image2 = base64.b64decode(p3_encodedimagelist2[-9])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

        if len(p3_titlelist2) >= 10 and p3_titlelist2[-10]:
            with st.expander(p3_titlelist2[-10]):
                st.write(p3_textlist2[-10])

                if p3_encodedimagelist2 and p3_encodedimagelist2[-10]:
                    decoded_image2 = base64.b64decode(p3_encodedimagelist2[-10])
                    display_image2 = Image.open(BytesIO(decoded_image2))
                    st.image(display_image2)

with tab3:
    if len(p3_titlelist3) < 1:
        st.write(
            "<p style='color:lightgrey;font-style:italic;'>아직 작성된 글이 없어요.</p>",
            unsafe_allow_html=True
        )
    else:
        if p3_titlelist3[-1]:
            with st.expander(p3_titlelist3[-1]):
                st.write(p3_textlist3[-1])

                if p3_encodedimagelist3 and p3_encodedimagelist3[-1]:
                    decoded_image3 = base64.b64decode(p3_encodedimagelist3[-1])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p3_titlelist3) >= 2 and p3_titlelist3[-2]:
            with st.expander(p3_titlelist3[-2]):
                st.write(p3_textlist3[-2])

                if p3_encodedimagelist3 and p3_encodedimagelist3[-2]:
                    decoded_image3 = base64.b64decode(p3_encodedimagelist3[-2])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p3_titlelist3) >= 3 and p3_titlelist3[-3]:
            with st.expander(p3_titlelist3[-3]):
                st.write(p3_textlist3[-3])

                if p3_encodedimagelist3 and p3_encodedimagelist3[-3]:
                    decoded_image3 = base64.b64decode(p3_encodedimagelist3[-3])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p3_titlelist3) >= 4 and p3_titlelist3[-4]:
            with st.expander(p3_titlelist3[-4]):
                st.write(p3_textlist3[-4])

                if p3_encodedimagelist3 and p3_encodedimagelist3[-4]:
                    decoded_image3 = base64.b64decode(p3_encodedimagelist3[-4])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p3_titlelist3) >= 5 and p3_titlelist3[-5]:
            with st.expander(p3_titlelist3[-5]):
                st.write(p3_textlist3[-5])

                if p3_encodedimagelist3 and p3_encodedimagelist3[-5]:
                    decoded_image3 = base64.b64decode(p3_encodedimagelist3[-5])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p3_titlelist3) >= 6 and p3_titlelist3[-6]:
            with st.expander(p3_titlelist3[-6]):
                st.write(p3_textlist3[-6])

                if p3_encodedimagelist3 and p3_encodedimagelist3[-6]:
                    decoded_image3 = base64.b64decode(p3_encodedimagelist3[-6])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p3_titlelist3) >= 7 and p3_titlelist3[-7]:
            with st.expander(p3_titlelist3[-7]):
                st.write(p3_textlist3[-7])

                if p3_encodedimagelist3 and p3_encodedimagelist3[-7]:
                    decoded_image3 = base64.b64decode(p3_encodedimagelist3[-7])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p3_titlelist3) >= 8 and p3_titlelist3[-8]:
            with st.expander(p3_titlelist3[-8]):
                st.write(p3_textlist3[-8])

                if p3_encodedimagelist3 and p3_encodedimagelist3[-8]:
                    decoded_image3 = base64.b64decode(p3_encodedimagelist3[-8])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p3_titlelist3) >= 9 and p3_titlelist3[-9]:
            with st.expander(p3_titlelist3[-9]):
                st.write(p3_textlist3[-9])

                if p3_encodedimagelist3 and p3_encodedimagelist3[-9]:
                    decoded_image3 = base64.b64decode(p3_encodedimagelist3[-9])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

        if len(p3_titlelist3) >= 10 and p3_titlelist3[-10]:
            with st.expander(p3_titlelist3[-10]):
                st.write(p3_textlist3[-10])

                if p3_encodedimagelist3 and p3_encodedimagelist3[-10]:
                    decoded_image3 = base64.b64decode(p3_encodedimagelist3[-10])
                    display_image3 = Image.open(BytesIO(decoded_image3))
                    st.image(display_image3)

