import streamlit as st
import numpy as np
import plotly.express as px


def load_rain_map(specific_date_df):
    rain_map_fig = px.density_mapbox(specific_date_df, lat='Latitude', lon='Longitude', z='Precipitation (Inches)', radius=10, center=dict(lat=np.median(
        specific_date_df['Latitude']), lon=np.median(specific_date_df['Longitude'])), mapbox_style="open-street-map", color_continuous_scale=['#c9fffc', '#030b7e'], title="Precipitation Map")
    st.plotly_chart(rain_map_fig, theme="streamlit", use_container_width=True)
