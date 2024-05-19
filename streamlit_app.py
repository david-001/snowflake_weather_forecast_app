# streamlit_app.py

import pandas as pd
import streamlit as st
import plotly.express as px

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Initialize connection.
conn = st.connection("snowflake")


# Perform database queries
countries = conn.query(
    "SELECT DISTINCT COUNTRY FROM onpoint_id.history_day ORDER BY COUNTRY")
# selected_country = countries.iloc[0]["COUNTRY"]
selected_country = st.selectbox(label="Country", options=countries)


cities = conn.query("SELECT DISTINCT CITY_NAME FROM onpoint_id.history_day WHERE COUNTRY = '" +
                    selected_country + "' ORDER BY CITY_NAME")
# selected_city = cities.iloc[0]["CITY_NAME"]
selected_city = st.selectbox(label="City", options=cities)

conn_str = f"""
  SELECT
    city_name,
    country,
    date_valid_std,
    avg_temperature_air_2m_f,
    tot_precipitation_in,
  FROM
      onpoint_id.history_day
  WHERE
      city_name = '{selected_city}' AND
      country = '{selected_country}'
  ORDER BY
      date_valid_std
      DESC
  LIMIT 14
  ;
  """

data_str = f"""
  CREATE OR REPLACE view temp_historic_data AS
    SELECT
        city_name,
        country,
        date_valid_std,
        avg_temperature_air_2m_f
      FROM
          onpoint_id.history_day
      WHERE
          city_name = '{selected_city}' AND
          country = '{selected_country}'
      ORDER BY
          date_valid_std
          DESC
      LIMIT 1000;
"""
# conn.query("USE SCHEMA your_WEATHER_SOURCE_LLC_FROSTBYTE.ONPOINT_ID")
# conn.query(data_str)

training_model_str = f"""
  CREATE or replace SNOWFLAKE.ML.FORECAST model_temp(
    INPUT_DATA => SYSTEM$REFERENCE('view', 'vw_gold_rate'),
    TIMESTAMP_COLNAME => 'date_valid_std',
    TARGET_COLNAME => 'avg_temperature_air_2m_f'
  );
"""
# conn.query(training_model_str)


def select_country(selected_country):
    cities = conn.query("SELECT DISTINCT CITY_NAME FROM onpoint_id.history_day WHERE COUNTRY = '" +
                        selected_country + "' ORDER BY CITY_NAME")
    return cities.iloc[0]["CITY_NAME"]


df = conn.query(conn_str, ttl=600)


# st.dataframe(selected_country)
# Convert the 'date' column to datetime format
# df['DATE_VALID_STD'] = pd.to_datetime(df['DATE_VALID_STD'])

# Set the 'date' column as the index
# df.set_index('DATE_VALID_STD', inplace=True)

st.dataframe(data=df)
# st.bar_chart(data=df, height=500)

# temp_tab, rain_tab = st.tabs(["Temperature", "Precipitation"])

# with temp_tab:
#     temp_fig = px.bar(df, x="DATE_VALID_STD", y="AVG_TEMPERATURE_AIR_2M_F", title="Temperature Forecast", labels={
#         "DATE_VALID_STD": "Date", "AVG_TEMPERATURE_AIR_2M_F": "Temperature (F)"})
#     st.plotly_chart(temp_fig, theme="streamlit", use_container_width=True)

# with rain_tab:
#     rain_fig = px.bar(df, x="DATE_VALID_STD", y="TOT_PRECIPITATION_IN", title="Precipitation Forecast", labels={
#         "DATE_VALID_STD": "Date", "TOT_PRECIPITATION_IN": "Precipitation (Inches)"})
#     st.plotly_chart(rain_fig, theme="streamlit", use_container_width=True)


# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=df["DATE_VALID_STD"],
               y=df["AVG_TEMPERATURE_AIR_2M_F"], name="Temperature (F)"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df["DATE_VALID_STD"],
               y=df["TOT_PRECIPITATION_IN"], name="Precipitation (Inches)"),
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text="Weather Forecast"
)

# Set x-axis title
fig.update_xaxes(title_text="Date")

# Set y-axes titles
fig.update_yaxes(title_text="Temperature (F)", secondary_y=False)
fig.update_yaxes(title_text="Precipation (Inches)", secondary_y=True)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)
