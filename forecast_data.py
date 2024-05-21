import streamlit as st
from create_connection import create_connection
from run_query import run_query
import pandas as pd


def forecast_data(conn, selected_city, selected_postal_code):

    # Join weather data and geo data
    combine_weather_geo_forecast_str = f"""
      SELECT DISTINCT forecast_day.date_valid_std, forecast_day.postal_code, forecast_day.avg_temperature_air_2m_f, forecast_day.tot_precipitation_in
      FROM forecast_day
      WHERE forecast_day.country = 'US' AND forecast_day.city_name = '{selected_city}' AND forecast_day.postal_code = '{selected_postal_code}'
      ORDER by forecast_day.date_valid_std ASC
    """

    forecast_data = run_query(conn, combine_weather_geo_forecast_str)
    forecast_df = pd.DataFrame(forecast_data, columns=[
                               'Date', 'Postcode', 'Temperature (F)', 'Precipitation (Inches)'])

    return forecast_df
