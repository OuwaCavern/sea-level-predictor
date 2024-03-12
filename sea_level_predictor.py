import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,4), dpi=100)
    ax.set_xlabel("year")
    ax.set_ylabel("CSIRO Adjusted Sea Level")
    df.plot(ax=ax, x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    res = linregress(x=df["Year"],y=df["CSIRO Adjusted Sea Level"])
    slope = 0.0630445840121348
    intercept = -119.06594196773978
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label = "data points" )
    plt.plot(df["Year"], y_line, label="Line of best fit")
    years_to_predict = np.arange(df["Year"].min(), 2051)
    predicted_sea_levels = slope * years_to_predict + intercept
    plt.figure(figsize=(10, 4), dpi=100)
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data points")
    plt.plot(df["Year"], slope * df["Year"] + intercept, label="Line of best fit")
    plt.plot(years_to_predict, predicted_sea_levels, label="Predicted sea levels (up to 2050)", color="red")
    plt.xlabel("Year")
    plt.ylabel("CSIRO Adjusted Sea Level")
    plt.legend()

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()