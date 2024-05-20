import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from temp_map import load_temp_map
from rain_map import load_rain_map
from get_weather import get_weather
from get_cities import get_cities
from get_dates import get_dates
from specific_date_data import specific_date_data


temp_forecast_tab, rain_forecast_tab, temp_map_tab, rain_map_tab = st.tabs(
    ["Temperature Forecast", "Precipitation Forecast", "Temperature Map", "Precipitation Map"])


def main():

    get_weather()
    selected_city = st.selectbox(label="City", options=get_cities())
    selected_date = st.selectbox(label="Date", options=get_dates())
    specific_date_df = specific_date_data(selected_city=selected_city,
                                          selected_date=selected_date)
    with temp_map_tab:
        load_temp_map(specific_date_df=specific_date_df)

    with rain_map_tab:
        load_rain_map(specific_date_df=specific_date_df)


if __name__ == "__main__":
    main()

    # Initialize connection.
    # conn = st.connection("snowflake")

    # get_countries_str = """
    #   SELECT DISTINCT forecast_day.country
    #   FROM forecast_day
    #   INNER JOIN address
    #   ON forecast_day.country = UPPER(address.country)
    #   ORDER BY forecast_day.country
    # """
    # countries = conn.query(get_countries_str)
    # selected_country = st.selectbox(label="Country", options=countries)

    # get_weather_db_str = """
    #   CREATE OR REPLACE TABLE GEO_WEATHER_DATA.GEO_WEATHER.FORECAST_DAY AS
    #   SELECT * FROM WEATHER_SOURCE_LLC_FROSTBYTE.ONPOINT_ID.FORECAST_DAY
    #   WHERE COUNTRY = 'US'
    #   AND DATE_VALID_STD BETWEEN CAST(GETDATE() AS DATE) AND CAST(DATEADD(day, 5, GETDATE()) AS DATE);
    # """
    # conn.query(get_weather_db_str)

    # get_cities_str = """
    #   SELECT DISTINCT forecast_day.city_name
    #   FROM forecast_day
    #   INNER JOIN address
    #   ON UPPER(forecast_day.city_name) = address.city
    #   ORDER BY forecast_day.city_name
    # """
    # cities = conn.query(get_cities_str)
    # selected_city = st.selectbox(label="City", options=cities)

    # # Join weather data and geo data
    # join_tables_conn_str = f"""
    #   SELECT forecast_day.date_valid_std, address.postcode, forecast_day.avg_temperature_air_2m_f, address.lat, address.lon, address.city, address.country
    #   FROM forecast_day
    #   INNER JOIN address
    #   ON forecast_day.postal_code = address.postcode
    #   WHERE forecast_day.country = 'US' AND forecast_day.city_name = '{selected_city}' AND forecast_day.date_valid_std = '2024-05-21'
    # """

    # df = conn.query(join_tables_conn_str)

    # st.dataframe(data=df)
    # st.bar_chart(data=df, height=500)

    # fig = px.density_mapbox(df, lat='LAT', lon='LON', z='AVG_TEMPERATURE_AIR_2M_F',
    #                         radius=10, center=dict(lat=0, lon=180), zoom=0, mapbox_style="open-street-map", color_continuous_scale=['#fffdc9', '#7e0327'])
    # st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    # # Perform database queries
    # countries = conn.query(
    #     "SELECT DISTINCT COUNTRY FROM geo_weather.forecast_day ORDER BY COUNTRY")
    # # selected_country = countries.iloc[0]["COUNTRY"]
    # selected_country = st.selectbox(label="Country", options=countries)

    # cities = conn.query("SELECT DISTINCT CITY_NAME FROM geo_weather.forecast_day WHERE COUNTRY = '" +
    #                     selected_country + "' ORDER BY CITY_NAME")
    # # selected_city = cities.iloc[0]["CITY_NAME"]
    # selected_city = st.selectbox(label="City", options=cities)

    # conn_str = f"""
    #   SELECT
    #     city_name,
    #     country,
    #     date_valid_std,
    #     avg_temperature_air_2m_f,
    #     tot_precipitation_in,
    #   FROM
    #       geo_weather.forecast_day
    #   WHERE
    #       city_name = '{selected_city}' AND
    #       country = '{selected_country}'
    #   ORDER BY
    #       date_valid_std
    #       DESC
    #   LIMIT 14
    #   ;
    #   """

    # data_str = f"""
    #   CREATE OR REPLACE view temp_historic_data AS
    #     SELECT
    #         city_name,
    #         country,
    #         date_valid_std,
    #         avg_temperature_air_2m_f
    #       FROM
    #           onpoint_id.forecast_day
    #       WHERE
    #           city_name = '{selected_city}' AND
    #           country = '{selected_country}'
    #       ORDER BY
    #           date_valid_std
    #           DESC
    #       LIMIT 1000;
    # """
    # # conn.query("USE SCHEMA your_WEATHER_SOURCE_LLC_FROSTBYTE.ONPOINT_ID")
    # # conn.query(data_str)

    # training_model_str = f"""
    #   # CREATE or replace SNOWFLAKE.ML.FORECAST model_temp(
    #   #   INPUT_DATA => SYSTEM$REFERENCE('view', 'vw_gold_rate'),
    #   #   TIMESTAMP_COLNAME => 'date_valid_std',
    #   #   TARGET_COLNAME => 'avg_temperature_air_2m_f'
    #   # );
    # """
    # # conn.query(training_model_str)

    # def select_country(selected_country):
    #     cities = conn.query("SELECT DISTINCT CITY_NAME FROM geo_weather.forecast_day WHERE COUNTRY = '" +
    #                         selected_country + "' ORDER BY CITY_NAME")
    #     return cities.iloc[0]["CITY_NAME"]

    # df = conn.query(conn_str, ttl=600)

    # # st.dataframe(selected_country)
    # # Convert the 'date' column to datetime format
    # # df['DATE_VALID_STD'] = pd.to_datetime(df['DATE_VALID_STD'])

    # # Set the 'date' column as the index
    # # df.set_index('DATE_VALID_STD', inplace=True)

    # st.dataframe(data=asd)

    # st.dataframe(data=df)
    # # st.bar_chart(data=df, height=500)

    # # temp_tab, rain_tab = st.tabs(["Temperature", "Precipitation"])

    # # with temp_tab:
    # #     temp_fig = px.bar(df, x="DATE_VALID_STD", y="AVG_TEMPERATURE_AIR_2M_F", title="Temperature Forecast", labels={
    # #         "DATE_VALID_STD": "Date", "AVG_TEMPERATURE_AIR_2M_F": "Temperature (F)"})
    # #     st.plotly_chart(temp_fig, theme="streamlit", use_container_width=True)

    # # with rain_tab:
    # #     rain_fig = px.bar(df, x="DATE_VALID_STD", y="TOT_PRECIPITATION_IN", title="Precipitation Forecast", labels={
    # #         "DATE_VALID_STD": "Date", "TOT_PRECIPITATION_IN": "Precipitation (Inches)"})
    # #     st.plotly_chart(rain_fig, theme="streamlit", use_container_width=True)

    # # Create figure with secondary y-axis
    # fig = make_subplots(specs=[[{"secondary_y": True}]])

    # # Add traces
    # fig.add_trace(
    #     go.Scatter(x=df["DATE_VALID_STD"],
    #                y=df["AVG_TEMPERATURE_AIR_2M_F"], name="Temperature (F)"),
    #     secondary_y=False,
    # )

    # fig.add_trace(
    #     go.Scatter(x=df["DATE_VALID_STD"],
    #                y=df["TOT_PRECIPITATION_IN"], name="Precipitation (Inches)"),
    #     secondary_y=True,
    # )

    # # Add figure title
    # fig.update_layout(
    #     title_text="Weather Forecast"
    # )

    # # Set x-axis title
    # fig.update_xaxes(title_text="Date")

    # # Set y-axes titles
    # fig.update_yaxes(title_text="Temperature (F)", secondary_y=False)
    # fig.update_yaxes(title_text="Precipation (Inches)", secondary_y=True)
    # st.plotly_chart(fig, theme="streamlit", use_container_width=True)
