#Data : https://meteo.data.gouv.fr/datasets/6569b3d7d193b4daf2b43edc

import streamlit as st
import pandas as pd
import numpy as np

st.title('Weather France')
st.write(
    """Personal project that compare the weather historical for some cities in France. These records are coming from meteo.data.gouv.fr   
      Basic climatological data - monthly
Presentation
Climatological data of all france stations since their opening, for all available parameters. The data underwent a climatological check.  
      These data are available via this [link](https://meteo.data.gouv.fr/datasets/6569b3d7d193b4daf2b43edc).
    """
)
st.sidebar.header("Weather France")

##Select data
Weather = pd.read_csv("Data/Weather_historical.csv")
Weather = Weather[["NUM_POSTE", "NOM_USUEL", "LAT", "LON", "ALTI", "AAAAMM", "RR", "NBJRR1" , "NBJRR5", "NBJRR10", "NBJRR30", "NBJRR50", "NBJRR100" ,"TX"," TN" ]]
Weather['NBJ_Pluie'] = Weather['NBJRR1'] + Weather['NBJRR5']  + Weather['NBJRR10'] + Weather['NBJRR30'] + Weather['NBJRR50']
Weather=Weather.rename(columns={"AAAAMM": "week", "RR": "Cumul_precipitation" ,"TX": "Temperature_max_AVG" , " TN": "Temperature_min_AVG"})
Weather =Weather.drop(columns=['NBJRR1', 'NBJRR5','NBJRR10','NBJRR30','NBJRR50'])
Weather['week'] = Weather['week'].astype(str)


#Show data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(Weather)


#selectbox selection for Y : Parameters
Y = st.sidebar.selectbox(
    "parameter",
    ("NBJ_Pluie","Cumul_precipitation", "Temperature_max_AVG", "Temperature_min_AVG")
)

#multiselect box for cities 
Cities = st.sidebar.multiselect(
    "Select the city",
    Weather['NOM_USUEL'].unique(),
    default=Weather['NOM_USUEL'].unique())
DF_weather = Weather.loc[Weather['NOM_USUEL'].isin(Cities)]


#Curve diagram
st.subheader( Y + ' per cities in France')
st.line_chart(DF_weather,x="week", y=Y,color ="NOM_USUEL" )


