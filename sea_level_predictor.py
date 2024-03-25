import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', parse_dates=True)
    # Create scatter plot
    # The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y, color='blue')
    
    # Create first line of best fit
    result = linregress(x.to_numpy(), y.to_numpy())
    slope = result.slope
    intercept = result.intercept
    ext_years = pd.Series(range(1880,2051))
    line = [slope * i + intercept for i in ext_years]
    plt.plot(ext_years, line, '-', color='green')

    # Create second line of best fit
    cur_df = df.loc[(df['Year'] >= 2000)]
    x = cur_df['Year']
    y = cur_df['CSIRO Adjusted Sea Level']
    result = linregress(x.to_numpy(), y.to_numpy())
    slope = result.slope
    intercept = result.intercept
    ext_years = pd.Series(range(2000,2051))
    line = [slope * i + intercept for i in ext_years]
    plt.plot(ext_years, line, '-', color='red')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()