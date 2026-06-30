import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('gapminder(2007).csv')
print(data.head())
print(data.info())

avg_data = data.groupby(data['continent']).mean(numeric_only = True)
avg_data = avg_data.reset_index()
print(avg_data)

plt.bar(avg_data['continent'], avg_data['life_exp'], color = 'teal')
plt.xlabel('Continent')
plt.ylabel('Average Life Exp')
print(plt.show())

plt.bar(avg_data['continent'], avg_data['gdp_cap'], color = 'teal')
plt.xlabel('Continent')
plt.ylabel('Average GDP per capita')
print(plt.show())

sns.countplot(x = data['continent'], palette = 'winter')