import streamlit as st
from run_query import run_query


def get_cities(conn):
    get_cities_str = """
      SELECT DISTINCT forecast_day.city_name
      FROM forecast_day
      INNER JOIN address
      ON UPPER(forecast_day.city_name) = address.city
      ORDER BY forecast_day.city_name
    """
    cities_result = run_query(
        conn, get_cities_str)
    cities = [item[0] for item in cities_result]

    return cities
