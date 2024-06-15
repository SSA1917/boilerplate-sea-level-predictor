import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure()
    plt.scatter(x=df['Year'].array,y=df['CSIRO Adjusted Sea Level'].array)

    # Create first line of best fit
    reg = linregress(df['Year'].array,df['CSIRO Adjusted Sea Level'].array)
    x = np.arange(df['Year'].min(),2051,1)
    plt.plot(
        x,
        x*reg.slope+reg.intercept,
        color='black')

    # Create second line of best fit
    df_fit = df.loc[(df['Year'] >= 2000) & (df['Year'] <= df['Year'].max())]
    reg2 = linregress(df_fit['Year'].array,df_fit['CSIRO Adjusted Sea Level'].array)
    x2 = np.arange(df_fit['Year'].min(),2051,1)
    plt.plot(
        x2,
        x2*reg2.slope+reg2.intercept,
        color='red')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()