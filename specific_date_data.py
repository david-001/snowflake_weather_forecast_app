from run_query import run_query
import pandas as pd


def specific_date_data(conn, selected_city, selected_date):

    # Join weather data and geo data
    combine_weather_geo_str = f"""
      SELECT forecast_day.date_valid_std, address.postcode, forecast_day.avg_temperature_air_2m_f, forecast_day.tot_precipitation_in, address.lat, address.lon, address.city, address.country
      FROM forecast_day
      INNER JOIN address
      ON forecast_day.postal_code = address.postcode
      AND LOWER(forecast_day.country) = address.country
      WHERE forecast_day.country = 'US' AND forecast_day.city_name = '{selected_city}' AND forecast_day.date_valid_std = '{selected_date}'
    """

    specific_date_data = run_query(conn, combine_weather_geo_str)
    specific_date_df = pd.DataFrame(specific_date_data, columns=[
        'Date', 'Postcode', 'Temperature (F)', 'Precipitation (inch)', 'Latitude', 'Longitude', 'City', 'Country'])

    return specific_date_df
