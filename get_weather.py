import streamlit as st
import toml
from create_connection import create_connection
from run_query import run_query


def get_weather():
    config = toml.load("secrets.toml")
    # Connect to database
    conn = create_connection(config["geo_weather_data"])

    # Perform get weather data query
    get_weather_db_query = """
      CREATE OR REPLACE TABLE GEO_WEATHER_DATA.GEO_WEATHER.FORECAST_DAY AS
      SELECT * FROM WEATHER_SOURCE_LLC_FROSTBYTE.ONPOINT_ID.FORECAST_DAY
      WHERE COUNTRY = 'US'
      AND DATE_VALID_STD BETWEEN CAST(GETDATE() AS DATE) AND CAST(DATEADD(day, 5, GETDATE()) AS DATE);
    """
    run_query(conn, get_weather_db_query)
