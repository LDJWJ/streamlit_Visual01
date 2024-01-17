import streamlit as st
import pandas as pd
import numpy as np
	
st.title('뉴욕시의 Uber 픽업')
	
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
              'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
	
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
	
data_load_state = st.text('데이터 로딩중...')
data = load_data(10000)
data_load_state.text("완료!")
	
if st.checkbox('RAW 데이터 확인'):
    st.subheader('RAW 데이터')
    st.write(data)
	
st.subheader('시간별 픽업 횟수')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
	
hour_to_filter = st.slider('시간', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
	
st.subheader('일정 시간대의 픽업 지도 : %s:00' % hour_to_filter)
st.map(filtered_data)