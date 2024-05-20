import streamlit as st
import snowflake.connector
import toml

# Function to create a connection to a Snowflake database


@st.cache_resource
def create_connection(config_section):
    try:
        conn = snowflake.connector.connect(
            account=config_section["account"],
            user=config_section["user"],
            password=config_section["password"],
            database=config_section["database"],
            schema=config_section["schema"]
        )
        return conn
    except snowflake.connector.errors.ProgrammingError as e:
        st.error(f"Connection error: {e}")
        return None
