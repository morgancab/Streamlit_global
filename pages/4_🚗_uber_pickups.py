#Tutorial Page : https://docs.streamlit.io/get-started/tutorials/create-an-app

import streamlit as st
import pandas as pd
import numpy as np
 
st.title('Uber pickups in NYC')

st.sidebar.header("Uber pickups in NYC")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

#@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

#data view
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#Diagram bar
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,12))[0]
st.bar_chart(hist_values)

#Diagram bar
hour_to_filter = st.sidebar.slider('hour', 0, 23, (0, 23), 1) 
filtered_data = data[(data[DATE_COLUMN].dt.hour > hour_to_filter[0]) & (data[DATE_COLUMN].dt.hour < hour_to_filter[1])]
st.subheader(f'Map of all pickups between {hour_to_filter[0]}:00 and {hour_to_filter[1]}:59')
st.map(filtered_data)