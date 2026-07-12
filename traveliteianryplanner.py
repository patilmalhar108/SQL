import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = pd.read_csv('Weather_Dataset.csv')
print(data.head())
data_group = data.groupby('month').mean(numeric_only= True)
data_group = data_group.reset_index()
data_group.plot.area(x = 'month', y = 'Humidity', alpha = 0.6)
plt.plot(data['Temperature (C)'])
plt.ylabel('Temperature (C)')
plt.xlabel('Reading Numbers over time')
plt.show()