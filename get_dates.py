import streamlit as st
import toml
from create_connection import create_connection
from run_query import run_query


def get_dates():
    config = toml.load("secrets.toml")
    # Connect to database
    conn = create_connection(config["geo_weather_data"])

    get_dates_str = """
      SELECT DISTINCT date_valid_std
      FROM forecast_day
      ORDER by date_valid_std ASC
    """
    dates_result = run_query(
        conn, get_dates_str)
    dates = [item[0] for item in dates_result]

    return dates
