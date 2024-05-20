import streamlit as st
import numpy as np
import plotly.express as px


def load_temp_map(specific_date_df):
    # config = toml.load("secrets.toml")
    # # Connect to database
    # conn = create_connection(config["geo_weather_data"])

  #  # Perform get weather data query
  #   get_weather_db_query = """
  #   CREATE OR REPLACE TABLE GEO_WEATHER_DATA.GEO_WEATHER.FORECAST_DAY AS
  #   SELECT * FROM WEATHER_SOURCE_LLC_FROSTBYTE.ONPOINT_ID.FORECAST_DAY
  #   WHERE COUNTRY = 'US'
  #   AND DATE_VALID_STD BETWEEN CAST(GETDATE() AS DATE) AND CAST(DATEADD(day, 5, GETDATE()) AS DATE);
  # """
  #   run_query(conn, get_weather_db_query)

  #   get_cities_str = """
  #   SELECT DISTINCT forecast_day.city_name
  #   FROM forecast_day
  #   INNER JOIN address
  #   ON UPPER(forecast_day.city_name) = address.city
  #   ORDER BY forecast_day.city_name
  # """
  #   cities_result = run_query(
  #       conn, get_cities_str)
  #   cities = [item[0] for item in cities_result]

  #   selected_city = st.selectbox(label="City", options=cities)

  #   get_dates_str = """
  #   SELECT DISTINCT date_valid_std
  #   FROM forecast_day
  #   ORDER by date_valid_std ASC
  # """
  #   dates_result = run_query(
  #       conn, get_dates_str)
  #   dates = [item[0] for item in dates_result]

  #   selected_date = st.selectbox(label="Date", options=dates)

    # # Join weather data and geo data
    # combine_weather_geo_str = f"""
    #   SELECT forecast_day.date_valid_std, address.postcode, forecast_day.avg_temperature_air_2m_f, forecast_day.tot_precipitation_in, address.lat, address.lon, address.city, address.country
    #   FROM forecast_day
    #   INNER JOIN address
    #   ON forecast_day.postal_code = address.postcode
    #   AND LOWER(forecast_day.country) = address.country
    #   WHERE forecast_day.country = 'US' AND forecast_day.city_name = '{selected_city}' AND forecast_day.date_valid_std = '{selected_date}'
    # """

    # specific_date_data = run_query(conn, combine_weather_geo_str)
    # specific_date_df = pd.DataFrame(specific_date_data, columns=[
    #     'Date', 'Postcode', 'Temperature (F)', 'Precipitation (inch)', 'Latitude', 'Longitude', 'City', 'Country'])
    # st.dataframe(data=df)

    fig = px.density_mapbox(specific_date_df, lat='Latitude', lon='Longitude', z='Temperature (F)',
                            radius=10, center=dict(lat=np.median(specific_date_df['Latitude']), lon=np.median(specific_date_df['Longitude'])), mapbox_style="open-street-map", color_continuous_scale=['#fffdc9', '#7e0327'])
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
