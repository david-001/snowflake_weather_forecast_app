import streamlit as st
import numpy as np
import plotly.express as px


def load_temp_map(specific_date_df):
    temp_map_fig = px.density_mapbox(specific_date_df, lat='Latitude', lon='Longitude', z='Temperature (F)', radius=10, center=dict(lat=np.median(
        specific_date_df['Latitude']), lon=np.median(specific_date_df['Longitude'])), mapbox_style="open-street-map", color_continuous_scale=['#fffdc9', '#7e0327'], title="Temperature Map")
    st.plotly_chart(temp_map_fig, theme="streamlit", use_container_width=True)
