import streamlit as st
import snowflake.connector

# Function to create a connection to a Snowflake database


@st.cache_resource
def create_connection():
    try:
        conn = snowflake.connector.connect(
            account=st.secrets["geo_weather_data"]["account"],
            user=st.secrets["geo_weather_data"]["user"],
            password=st.secrets["geo_weather_data"]["password"],
            database=st.secrets["geo_weather_data"]["database"],
            arehouse=st.secrets["geo_weather_data"]["warehouse"],
            schema=st.secrets["geo_weather_data"]["schema"]
        )
        return conn
    except snowflake.connector.errors.ProgrammingError as e:
        st.error(f"Connection error: {e}")
        return None
