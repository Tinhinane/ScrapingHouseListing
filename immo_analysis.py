import csv
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import figure
import matplotlib.pyplot as plt


plt.style.use('bmh')

df = pd.read_csv('test_data.csv');
df.head()
df.info()

print('Description of the price :')
print(df['Price'].describe())
plt.figure(figsize=(9, 8))
sns.distplot(df['Price'], bins=100,hist_kws={'alpha': 0.4},color='g');
#x = np.random.normal(size=100)
#sns.distplot(x);
plt.show()
