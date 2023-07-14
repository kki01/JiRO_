import streamlit as st
import boto3
import base64
import gspread
from google.oauth2.service_account import Credentials
from google.oauth2 import service_account
from PIL import Image
from datetime import date, timedelta
from gspread.utils import a1_range_to_grid_range

st.set_page_config(
    page_title="JiRO.com",
    page_icon="🏫"  
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
# 새 글 작성
###########################################################################################################

st.markdown('<h4 style="text-align: center;">새 글 작성</h4>', unsafe_allow_html=True)
st.divider()

writting = st.selectbox('대계열을 선택하세요.', ('공학계열', '교육계열', '사회계열', '예체능계열', '의약계열', '인문계열', '자연계열'))

middlecategory = ('교육일반', '유아교육', '중등교육', '초등교육', '특수교육학')

if writting == '공학계열':
    writting_category = 'page-1'
    middlecategory = ('건축', '교통·운송', '기계·금속', '산업', '소재·재료', '전기·전자', '정밀·에너지', '컴퓨터·통신', '토목·도시', '화공', '기타')
elif writting == '교육계열':
    writting_category = 'page-2'
    middlecategory = ('교육일반', '유아교육', '중등교육', '초등교육', '특수교육학')
elif writting == '사회계열':
    writting_category = 'page-3'
    middlecategory = ('경영·경제', '법률', '사회과학')
elif writting == '예체능계열':
    writting_category = 'page-4'
    middlecategory = ('디자인', '무용·체육', '미술·조형', '연극·영화', '음악', '응용예술')
elif writting == '의약계열':
    writting_category = 'page-5'
    middlecategory = ('간호', '약학', '의료', '치료·보건')
elif writting == '인문계열':
    writting_category = 'page-6'
    middlecategory = ('언어·문학', '인문과학')
elif writting == '자연계열':
    writting_category = 'page-7'
    middlecategory = ('농림·수산', '생물·화학·환경', '생활과학', '수학·물리·천문·지리')

writting_category_middle = st.selectbox('중계열을 선택하세요.', middlecategory)
title = st.text_input("제목")
text = st.text_area("본문")

with st.expander("이미지 업로드"):
    uploaded_file = st.file_uploader("해상도가 너무 높은 파일은 오류가 발생할 수 있습니다.", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image_data = uploaded_file.read()
        encoded_image = base64.b64encode(image_data).decode("utf-8")

        image = Image.open(uploaded_file)
        st.image(image)

st.caption("다른 페이지로 이동하면 작성 중인 내용이 모두 사라지니 주의하세요.")
st.divider()

if st.button("업로드"):
    if not title:
        st.error("제목을 입력하세요.")
    else:
        if not text:
            st.error("본문을 입력하세요.")
        else:
            if uploaded_file: # 파일 존재
                datalist = [title, text, writting_category, writting_category_middle, encoded_image]
            
            else:
                datalist = [title, text, writting_category, writting_category_middle]

            try:
                worksheet.append_row(datalist)
                st.success("성공적으로 업로드되었습니다.")
            except Exception as e:
                st.error("오류가 발생하였습니다. 다시 시도해 주세요.")
                st.caption("1. 크기가 너무 큰 이미지는 인코딩 중 오류가 발생할 수 있습니다. 업로드할 이미지 파일의 크기를 줄여 보세요.\n2. 네트워크 상태가 양호한지 확인해 주세요.")
#               st.error(str(e))