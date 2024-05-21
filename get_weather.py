import streamlit as st
from run_query import run_query


def get_weather(conn):
    # Perform get weather data query
    get_weather_db_query = """
      CREATE OR REPLACE TABLE GEO_WEATHER_DATA.GEO_WEATHER.FORECAST_DAY AS
      SELECT * FROM WEATHER_SOURCE_LLC_FROSTBYTE.ONPOINT_ID.FORECAST_DAY
      WHERE COUNTRY = 'US'
      AND DATE_VALID_STD BETWEEN CAST(GETDATE() AS DATE) AND CAST(DATEADD(day, 10, GETDATE()) AS DATE);
    """
    run_query(conn, get_weather_db_query)
