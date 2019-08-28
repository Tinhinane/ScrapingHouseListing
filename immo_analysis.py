import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype

plt.style.use('bmh')
df = pd.read_csv("immoweb.csv",encoding = "ISO-8859-1")
df.Price = df.Price.fillna(0)
print(df.groupby('Title').mean()['Price'].astype(int).sort_values())
sns.boxplot(x='Zip', y='Price', data=df)
plt.xlabel("Zip")
plt.xticks(rotation=75)
plt.ylabel("Price Euro")
plt.title("Prices by Neighborhood")
plt.show()