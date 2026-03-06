import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from scipy.stats import linregress

st.title("Sea Level Predictor 🌊")

df = pd.read_csv("epa-sea-level.csv")

plt.figure(figsize=(10,5))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# First regression line
res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years = range(df['Year'].min(), 2051)
plt.plot(years, res.intercept + res.slope * pd.Series(years), 'r')

plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")

st.pyplot(plt)