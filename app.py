import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from scipy.stats import linregress
import numpy as np

st.set_page_config(page_title="Sea Level Predictor", layout="wide")

st.title("🌊 Sea Level Predictor")

# -------- FILE UPLOAD --------
uploaded_file = st.file_uploader("📂 Upload Sea Level Dataset (CSV)", type="csv")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

    # -------- CLEAN --------
    df = df.dropna()

    # -------- PLOT --------
    st.subheader("📈 Sea Level Trend")

    fig, ax = plt.subplots(figsize=(10,5))

    # Scatter
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, label="Data")

    # -------- FULL DATA REGRESSION --------
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_full = np.arange(df['Year'].min(), 2051)

    ax.plot(
        years_full,
        res1.intercept + res1.slope * years_full,
        color="red",
        label="Full Trend"
    )

    # -------- RECENT DATA REGRESSION (after 2000) --------
    df_recent = df[df['Year'] >= 2000]

    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)

    ax.plot(
        years_recent,
        res2.intercept + res2.slope * years_recent,
        color="green",
        label="Recent Trend (2000+)"
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)

    st.pyplot(fig)

    # -------- FUTURE PREDICTION --------
    st.subheader("🔮 Future Prediction")

    future_year = st.slider("Select Year", 2025, 2050, 2030)

    predicted_level = res2.intercept + res2.slope * future_year

    st.success(f"📊 Predicted Sea Level in {future_year}: {predicted_level:.2f} inches")

else:
    st.info("👆 Upload a CSV file to get started")
