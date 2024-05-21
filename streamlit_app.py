import streamlit as st
from create_connection import create_connection
from temp_map import load_temp_map
from rain_map import load_rain_map
from get_weather import get_weather
from get_cities import get_cities
from get_dates import get_dates
from get_postal_codes import get_postal_codes
from specific_date_data import specific_date_data
from forecast_data import forecast_data
from forecast import load_forecast

st.title("US Weather Forecast")
# Connect to database
conn = create_connection()
get_weather(conn)
selected_city = st.selectbox(label="City", options=get_cities(conn))
selected_date = st.selectbox(label="Date", options=get_dates(conn))
selected_postal_code = st.selectbox(
    label="Postal Code", options=get_postal_codes(conn, selected_city=selected_city))
specific_date_df = specific_date_data(
    conn, selected_city=selected_city, selected_date=selected_date)
forecast_df = forecast_data(
    conn, selected_city=selected_city, selected_postal_code=selected_postal_code)

if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 'Forecast'

forecast_tab, temp_map_tab, rain_map_tab = st.tabs(
    ["Forecast", "Temperature Map", "Precipitation Map"])


def main():

    with forecast_tab:
        load_forecast(forecast_df=forecast_df)

    with temp_map_tab:
        load_temp_map(specific_date_df=specific_date_df)

    with rain_map_tab:
        load_rain_map(specific_date_df=specific_date_df)


if __name__ == "__main__":
    main()
