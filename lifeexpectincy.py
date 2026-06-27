import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('gapminder(2007).csv')
print(data.head())
print(data.info())
print(data.isnull().any())

sns.scatterplot(data = data, x = 'gdp_cap', y = 'life_exp')
print(plt.show())

sns.scatterplot(data = data, x = 'gdp_cap', y = 'life_exp', hue = 'continent')
print(plt.show())

fig, ax = plt.subplots(figsize = (8,8))
sns.scatterplot(data = data, x = 'gdp_cap', y = 'life_exp', size = 'population', alpha = 0.7,
hue = 'continent', sizes = (20,1000),palette = 'bright')
print(plt.show())

sns.heatmap(data.corr(numeric_only=True), annot=True)
plt.show()

sns.relplot(data = data, y = 'life_exp', x = 'gdp_cap', col = 'continent', col_wrap = 3, height = 3)
print(plt.show())

sns.pairplot(data, hue = 'continent')
print(plt.show())