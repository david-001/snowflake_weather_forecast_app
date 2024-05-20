import streamlit as st
from create_connection import create_connection
from run_query import run_query


def get_dates():
    # Connect to database
    conn = create_connection()

    get_dates_str = """
      SELECT DISTINCT date_valid_std
      FROM forecast_day
      ORDER by date_valid_std ASC
    """
    dates_result = run_query(
        conn, get_dates_str)
    dates = [item[0] for item in dates_result]

    return dates
