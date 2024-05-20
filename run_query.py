import streamlit as st
import snowflake.connector

# Function to query the database


def run_query(connection, query):
    try:
        cur = connection.cursor()
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        return results
    except snowflake.connector.errors.ProgrammingError as e:
        st.error(f"Query error: {e}")
        return []
