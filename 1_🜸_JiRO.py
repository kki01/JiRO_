import streamlit as st
import boto3
from PIL import Image



### settings ###







st.set_page_config(
    page_title="JiRO.com",
    page_icon="🏫"  
)

### 이미지 불러오기 ###

introduction_image = Image.open("title_image.png")
logo = Image.open("JiRO.png")
dec_image1 = Image.open("dec_image1.png")
dec_image2 = Image.open("dec_image2.png")

###########################################################################################################
# sidebar
###########################################################################################################


###########################################################################################################
# main page 
###########################################################################################################

st.image(logo) # 타이틀

tab1, tab2= st.tabs(["introduction", "patch notes"])

with tab1:
    
    st.write("※ This was created for a school assignment.")
    col1, col2 = st.columns([0.7, 0.3])

    with col1:
        st.image(introduction_image)
    
    with col2:
        with st.container():
            st.markdown('<h3 style="text-align: center;">WELCOME!</h3>', unsafe_allow_html=True)

        with st.container():
            st.write("JiRO는 학생들을 위한 진로 커뮤니티입니다. 같은 계열의 학과를 지망하는 학생들과 정보를 공유하고 교류할 수 있습니다. 교내 행사, 외부 프로그램, 유익한 자료나 영상 등, 공유하고 싶은 것이 있다면 회원 가입이나 로그인 없이도 몇 번의 클릭만으로 공유할 수 있습니다.")

        with st.container():
            st.write("진로가 아직 정해지지 않은 학생이라도 다양한 글을 둘러보고 자신의 삶의 방향을 정해보세요!")

    st.divider()

    col1, col2 = st.columns([0.3, 0.7])

    with col1:
        with st.container():
            st.markdown('<h3 style="text-align: center;">SHARING</h3>', unsafe_allow_html=True)        
        with st.container():
            st.write("자신이 가진 유용한 정보와 소식을 공유하세요. 계열별로 가장 최근에 작성된 글을 최대 10개까지 열람할 수 있습니다. 다양한 소식을 접하고 다양한 경험을 쌓아보세요!")

    with col2:
        st.image(dec_image1)

    st.divider()
    col1, col2 = st.columns([0.7, 0.3])

    with col1:
        st.image(dec_image2)

    with col2:
        with st.container():
            st.markdown('<h3 style="text-align: center;">WRITTING</h3>', unsafe_allow_html=True)        
        with st.container():
            st.write("직관적이고 간편한 글 에디터로 글을 작성하세요. 계열을 선택하고 글을 작성합니다. 제목, 본문 모두 최대 50000자까지 작성이 가능합니다. 이미지를 최대 1개까지 첨부할 수 있습니다. (해상도가 높은 이미지는 오류가 발생할 수 있습니다.)")
        with st.container():
            st.write("<주의> 현재 이미 업로드한 글은 수정/삭제 기능을 지원하지 않습니다. 신중히 생각하고 글을 작성해주세요.")
    
    st.divider()

with tab2:
    with st.container():
        st.write(" ")
        st.write("⯌ 2023-07-13 로고 변경")
        st.write("⯌ 2023-07-14 게시판 세분화")
        st.write(" ")
        st.divider()
        st.write(
        "<p style='text-align:right;'>마지막 업데이트: 2023.07.14</p>",
        unsafe_allow_html=True
    )
        st.write(
        "<p style='text-align:right;'>(학번: 10320) made with streamlit</p>",
        unsafe_allow_html=True
    )
