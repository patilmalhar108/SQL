import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('gapminder(2007).csv')
print(data.head())
data.groupby('continent').size().plot(kind = 'pie', autopct = '%.2f')
#plt.figure(figsize = (8,8))
#plt.fill(data.groupby(), labels = data.groupby().index, startangle = 90)
plt.pie(data.groupby('continent').size(), autopct = '%.2f', labels = ['Africa', 'America', 'Asia',
'Europe', 'Oceania'], labeldistance = 1.15, wedgeprops = {'linewidth':2, 'edgecolor':'white'})
plt.show()