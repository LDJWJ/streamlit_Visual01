import streamlit as st

# 제목과 서브헤더
st.title("나의 첫 Streamlit 앱")
st.subheader("여기에 서브헤더를 추가할 수 있습니다.")

# 텍스트 출력
st.write("안녕하세요! 이것은 간단한 Streamlit 애플리케이션입니다.")

# 숫자 입력 받기
number = st.number_input("숫자를 입력하세요", 
                         min_value=0, max_value=100, value=0)

st.write(f"입력한 숫자는 {number}입니다.")

# 버튼 만들기
if st.button("버튼 클릭"):
    st.write("버튼이 클릭되었습니다!")

# 셀렉트 박스
option = st.selectbox("옵션을 선택하세요", ["옵션 1", "옵션 2", "옵션 3"])
st.write(f"선택한 옵션: {option}")

# 그래프 그리기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"]
)

# 라인 차트
st.line_chart(data)


# 이미지 표시
 
# import Image from pillow to open images
from PIL import Image
img = Image.open("dog_01.jpg")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)

# Check Box
if st.checkbox("Show/Hide"):
 
    # display the text if the checkbox returns True value
    st.text("Showing the widget")

# Slider
level = st.slider("Select the level", 1, 5)
 
# print the level
# format() is used to print value 
# of a variable at a specific position
st.text('Selected: {}'.format(level))