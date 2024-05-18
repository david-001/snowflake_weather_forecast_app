# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("snowflake")



# Perform database queries
countries = conn.query("SELECT DISTINCT COUNTRY FROM onpoint_id.forecast_day ORDER BY COUNTRY")
# selected_country = countries.iloc[0]["COUNTRY"]
selected_country = st.selectbox(label="Country", options=countries)


cities = conn.query("SELECT DISTINCT CITY_NAME FROM onpoint_id.forecast_day WHERE COUNTRY = '" + selected_country + "' ORDER BY CITY_NAME")
# selected_city = cities.iloc[0]["CITY_NAME"]
selected_city = st.selectbox(label="City", options=cities)

conn_str = f"""
  SELECT
      city_name,
      country,
      date_valid_std,
      avg_temperature_air_2m_f,
      avg_humidity_relative_2m_pct,
      avg_wind_speed_10m_mph,
      tot_precipitation_in,
      tot_snowfall_in,
      avg_cloud_cover_tot_pct,
      probability_of_precipitation_pct,
      probability_of_snow_pct
  FROM
  (
      SELECT
          city_name,
          country,
          date_valid_std,
          avg_temperature_air_2m_f,
          avg_humidity_relative_2m_pct,
          avg_wind_speed_10m_mph,
          tot_precipitation_in,
          tot_snowfall_in,
          avg_cloud_cover_tot_pct,
          probability_of_precipitation_pct,
          probability_of_snow_pct,
          DATEADD(DAY,2,CURRENT_DATE()) AS skip_date,
          DATEADD(DAY,7 - DAYOFWEEKISO(skip_date),skip_date) AS next_sunday,
          DATEADD(DAY,-1,next_sunday) AS next_saturday
      FROM
          onpoint_id.forecast_day
      WHERE
          city_name = '{selected_city}' AND
          country = '{selected_country}'
  )
  WHERE
      date_valid_std IN (next_saturday,next_sunday)
  ORDER BY
      date_valid_std
  ;
  """

print(conn_str)

# conn_str ="""
# SELECT
#     {},
#     {},
#     date_valid_std,
#     avg_temperature_air_2m_f,
#     avg_humidity_relative_2m_pct,
#     avg_wind_speed_10m_mph,
#     tot_precipitation_in,
#     tot_snowfall_in,
#     avg_cloud_cover_tot_pct,
#     probability_of_precipitation_pct,
#     probability_of_snow_pct
# FROM
# (
#     SELECT
#         {},
#         {},
#         date_valid_std,
#         avg_temperature_air_2m_f,
#         avg_humidity_relative_2m_pct,
#         avg_wind_speed_10m_mph,
#         tot_precipitation_in,
#         tot_snowfall_in,
#         avg_cloud_cover_tot_pct,
#         probability_of_precipitation_pct,
#         probability_of_snow_pct,
#         DATEADD(DAY,2,CURRENT_DATE()) AS skip_date,
#         DATEADD(DAY,7 - DAYOFWEEKISO(CURRENT_DATE()),DATEADD(DAY,2,CURRENT_DATE())) AS next_sunday,
#         DATEADD(DAY,-1,DATEADD(DAY,7 - DAYOFWEEKISO(CURRENT_DATE()),DATEADD(DAY,2,CURRENT_DATE()))) AS next_saturday
#     FROM
#         onpoint_id.forecast_day
#     WHERE
#         postal_code = '02201' AND
#         country = 'US'
# )
# WHERE
#     date_valid_std IN (next_saturday,next_sunday)
# ORDER BY
#     date_valid_std
# ;
# """.format(selected_city,selected_country,selected_city,selected_country)

def select_country(selected_country):
  cities = conn.query("SELECT DISTINCT CITY_NAME FROM onpoint_id.forecast_day WHERE COUNTRY = '" + selected_country + "' ORDER BY CITY_NAME")
  return cities.iloc[0]["CITY_NAME"]

df = conn.query(conn_str, ttl=600)


# st.dataframe(selected_country)

st.dataframe(data=df)

