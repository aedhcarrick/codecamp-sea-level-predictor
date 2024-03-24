import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', parse_dates=True)
    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)
    # Create first line of best fit
    result = linregress(x.to_numpy(), y.to_numpy())
    slope = result.slope
    intercept = result.intercept
    plt.plot(x, intercept + slope * x, '-')

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()