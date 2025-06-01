#                Sea Level Predictor

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', color='blue')

    # Line of best fit for all data
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = pd.Series(range(1880, 2051))
    y_all = res_all.slope * x_all + res_all.intercept
    plt.plot(x_all, y_all, 'r', label='Fit: 1880–2050')

    # Line of best fit from year 2000
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    plt.plot(x_recent, y_recent, 'green', label='Fit: 2000–2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save and return the plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()

plt.show()