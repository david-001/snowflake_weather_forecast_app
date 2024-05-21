import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def load_forecast(forecast_df):
    st.dataframe(forecast_df)

    # Create figure with secondary y-axis
    forecast_fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    forecast_fig.add_trace(
        go.Scatter(x=forecast_df["Date"],
                   y=forecast_df["Temperature (F)"], name="Temperature (F)"),
        secondary_y=False,
    )

    forecast_fig.add_trace(
        go.Scatter(x=forecast_df["Date"],
                   y=forecast_df["Precipitation (Inches)"], name="Precipitation (Inches)"),
        secondary_y=True,
    )

    # Add figure title
    forecast_fig.update_layout(
        title_text="Weather Forecast"
    )

    # Set x-axis title
    forecast_fig.update_xaxes(title_text="Date")

    # Set y-axes titles
    forecast_fig.update_yaxes(title_text="Temperature (F)", secondary_y=False)
    forecast_fig.update_yaxes(
        title_text="Precipation (Inches)", secondary_y=True)
    st.plotly_chart(forecast_fig, theme="streamlit", use_container_width=True)
