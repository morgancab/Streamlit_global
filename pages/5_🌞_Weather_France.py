#Data : https://meteo.data.gouv.fr/datasets/6569b3d7d193b4daf2b43edc

import streamlit as st
import pandas as pd
import numpy as np


st.title('Weather France')

st.sidebar.header("Weather France")

##Select data
Weather = pd.read_csv("Data/Weather_historical.csv")
Weather = Weather[["NUM_POSTE", "NOM_USUEL", "LAT", "LON", "ALTI", "AAAAMM", "RR", "NBJRR1" , "NBJRR5", "NBJRR10", "NBJRR30", "NBJRR50", "NBJRR100" ,"TX"," TN" ]]
Weather['NBJ_Pluie'] = Weather['NBJRR1'] + Weather['NBJRR5']  + Weather['NBJRR10'] + Weather['NBJRR30'] + Weather['NBJRR50']
Weather=Weather.rename(columns={"AAAAMM": "week", "RR": "Cumul_precipitation" ,"TX": "Temperature_max_AVG" , " TN": "Temperature_min_AVG"})
Weather =Weather.drop(columns=['NBJRR1', 'NBJRR5','NBJRR10','NBJRR30','NBJRR50'])

#Show data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(Weather)


#Curve diagram
st.subheader('Number of pickups by hour')
st.line_chart(Weather,x="week", y="Cumul_precipitation",color ="NOM_USUEL" )
