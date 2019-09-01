import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype

plt.style.use('bmh')
df = pd.read_csv("clean_data_test.csv",encoding = "ISO-8859-1")
'''1. Histogram : House prices in BXL area
Step 01: Get the min and max of your data set
min = 35.000
max = 680.0000
Step 02: Define the binwidth
(you test till you find the right binwidth)
binwidth = 10.000
Step 03: Draw your Histogram
For this plot, I will use bins that are 10.000 euros in length,
which means that the number of bins will be the range of the data (from 30.000 to 680.000)
divided by the binwidth, 40.000 euros (bins = int(645000/10000) IMPORTANT: bins must be integers in seaborn)
(see https://en.wikipedia.org/wiki/Histogram)
'''
print(df['Price'].describe())
print('===DONE===')
# Draw the plot
binwidth = 50000
plt.hist(df['Price'], bins = int(645000/binwidth),
         color = 'blue', edgecolor = 'black')
# Title and labels
plt.title('Histogram of house prices in Brussels area')
plt.xlabel('Prices (Euro)')
plt.ylabel('Frequency')
plt.show()
'''First of all let's look at the distribution of house pricing regardeless of the appartment's surface'''
'''2. Density plot: House prices in BXL area
- The x-axis is the value of the variable just like in a histogram
- The y-axis in is the probability density function
The probability density function is nonnegative everywhere,
and its integral over the entire space is equal to one.
(see https://en.wikipedia.org/wiki/Probability_density_function)

Explanation: How to convert to an actual probability?
we need to find the area under the curve for a specific interval on the x-axis.
NOTE THAT: Because this is a probability density and not a probability, the y-axis can take
values greater than one.
==> The only requirement of the density plot is that the total area under the curve integrates to one.
'''
# sns.distplot(df['Price'], hist=False, kde=True,
#             bins=int(645000/binwidth), color = 'darkblue',
#             kde_kws={'linewidth': 4})
# #Plot formatting
# plt.title('Density Plot for house prices in BXL')
# plt.xlabel('Price (euro)')
# plt.ylabel('Density')
# plt.show()
#Will now let seaborn choose a reasonable value of the bandwidth for us by default using
#the ‘scott’ estimate
sns.distplot(df['Price'], hist=False, kde=True,
            color = 'blue',
            kde_kws={'linewidth': 4})
#Plot formatting
plt.title('Density Plot for house prices in BXL (default)')
plt.xlabel('Price (euro)')
plt.ylabel('Density')
plt.show()
'''
3. Density plot of house prices of multiple BXL Neighborhoods
'''
#List of neighborhoods to plot
zips = [1620, 1630, 1180]
# Iterate through the five airlines
for zip in zips:
    # Subset to the airline
    subset = df[df['Zip'] == zip]
    print(subset)
    # Draw the density plot
    sns.distplot(subset['Price'], hist = False, kde = True,
                 kde_kws = {'linewidth': 3},
                 label = zip)

# Plot formatting
plt.legend(prop={'size': 16}, title = 'Neighborhood')
plt.title('Density Plot with Multiple neighborhoods')
plt.xlabel('Price (euro)')
plt.ylabel('Density')
plt.show()

'''Now, let's take a look at the price vs size relationship
https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/
https://www.youtube.com/watch?v=owI7zxCqNY0
Y variable (dependent variable): price, this is the value we want to explain (or in another case forcast)
X variable (independant variable): surface, this is the value that explains the other value (price)
'''
'''Low priority https://github.com/codeforamerica/click_that_hood'''
sns.lmplot(x='Surface', y='Price', data=df, aspect=2)
plt.title('Regression analysis of house pricing')
plt.xlabel('Surface')
plt.ylabel('Price (euro)')
plt.show()
#Asma's part
'''
df.Price = df.Price.fillna(0)
print(df.groupby('Title').mean()['Price'].astype(int).sort_values())
sns.boxplot(x='Zip', y='Price', data=df)
plt.xlabel("Zip")
plt.xticks(rotation=75)
plt.ylabel("Price Euro")
plt.title("Prices by Neighborhood")
plt.show()
'''
