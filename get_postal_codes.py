import streamlit as st
from run_query import run_query


def get_postal_codes(conn, selected_city):
    get_postal_codes_str = f"""
      SELECT DISTINCT forecast_day.postal_code
      FROM forecast_day
      INNER JOIN address
      ON UPPER(forecast_day.postal_code) = address.postcode
      WHERE forecast_day.country = 'US' and forecast_day.city_name='{selected_city}'
      ORDER BY forecast_day.postal_code
    """
    postal_codes_result = run_query(
        conn, get_postal_codes_str)
    postal_codes = [item[0] for item in postal_codes_result]

    return postal_codes
