import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

house_df = pd.read_csv('USA_Housing.csv')
house_df.head()
house_df.info()
house_df.columns

sns.pairplot(house_df)
sns.heatmap(house_df.corr(), annot = True)