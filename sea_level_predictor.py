import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig = plt.figure()
    ax = plt.axes()
    plt.ax = plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    x_ext = df["Year"].append(pd.Series(range(2014,2051)))
    res = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    ax.plot(x_ext, res.intercept + res.slope*x_ext)

    # Create second line of best fit
    x_ext2000 = df["Year"].loc[df["Year"]>=2000].append(pd.Series(range(2014,2051)))
    res2000 = linregress(x=df["Year"].loc[df["Year"]>=2000], y=df["CSIRO Adjusted Sea Level"].loc[df["Year"]>=2000])
    ax.plot(x_ext2000, res2000.intercept + res2000.slope*x_ext2000)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()