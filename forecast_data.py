import streamlit as st
from create_connection import create_connection
from run_query import run_query
import pandas as pd


def forecast_data(conn, selected_city):

    # Join weather data and geo data
    combine_weather_geo_forecast_str = f"""
      SELECT forecast_day.date_valid_std, address.postcode, forecast_day.avg_temperature_air_2m_f, forecast_day.tot_precipitation_in, address.lat, address.lon, address.city, address.country
      FROM forecast_day
      INNER JOIN address
      ON forecast_day.postal_code = address.postcode
      AND LOWER(forecast_day.country) = address.country
      WHERE forecast_day.country = 'US' AND forecast_day.city_name = '{selected_city}'
    """

    forecast_data = run_query(conn, combine_weather_geo_forecast_str)
    forecast_df = pd.DataFrame(forecast_data, columns=[
                               'Date', 'Postcode', 'Temperature (F)', 'Precipitation (inch)', 'Latitude', 'Longitude', 'City', 'Country'])

    return forecast_df
