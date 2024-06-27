import requests
import json 
import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np
 
st.title('Rennes live Bike station ')

st.write(
    """This Streamlit page displays real-time information about the operational status of bike stations in Rennes. 
    It leverages the API provided by the city, accessible via this [link](https://data.rennesmetropole.fr/explore/dataset/etat-des-stations-le-velo-star-en-temps-reel/api/). 
    By utilizing this API, the page presents up-to-date details on bike availability and station status, providing
     users with a convenient and interactive way to find working bike stations in Rennes.
    """
)


## Collect data
response = requests.get("https://data.rennesmetropole.fr/api/explore/v2.1/catalog/datasets/etat-des-stations-le-velo-star-en-temps-reel/records?limit=20&timezone=europe%2FParis") 
st.write(
    'Response from the API : ', response
)

Dump_data = json.dumps(response.json())
Loads_data = json.loads(Dump_data)  
DF_bike_station = pd.json_normalize(Loads_data['results'])

#rename column
DF_bike_station=DF_bike_station.rename(columns={"nom": "Name" ,
                                                "etat": "status",
                                                "nombreemplacementsactuels": "Total space"  ,
                                                "nombreemplacementsdisponibles": "Available space"  ,
                                                "nombrevelosdisponibles": "Bike available"  ,
                                                "coordonnees.lon": "LON",
                                                "coordonnees.lat": "LAT" })

st.write(
    'API refreshed at : ', DF_bike_station['lastupdate'].max()
)

#Show data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(DF_bike_station)

#st.map(DF_bike_station)

# Create map 
st.subheader('Map showing the available bikes')

fig = px.scatter_mapbox(DF_bike_station, 
                        lat=DF_bike_station['LAT'],
                        lon=DF_bike_station['LON'], 
                        hover_name="Name", 
                        size="Bike available" ,
                        #hover_data=["status" , "Bike available" , "Available space" ],
                        custom_data=['Name', 'Bike available', 'Available space' , 'status'] ,
                        color="Bike available",
                        color_continuous_scale=px.colors.sequential.Emrld ,
                        opacity = 0.8,
                        zoom=12, 
                        height=450)
fig.update_layout(mapbox_style="carto-positron")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_layout(coloraxis_showscale=False)
fig.update_traces(
    hovertemplate = 
                "<b>%{customdata[0]}</b><br>"   +  
                "<b>Status: </b> %{customdata[3]}<br>" + 
                "<b>Number of bike: </b> %{customdata[1]}<br>" +
                "<b>Number of Space: </b> %{customdata[2]}<br>"  ) 

st.plotly_chart(fig)