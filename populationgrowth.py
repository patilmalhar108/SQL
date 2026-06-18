import pandas as pd
import matplotlib.pyplot as plt
countries_df = pd.read_csv('country_data.csv')
countries = countries_df
print(countries.head(3))
c_1952 = countries.loc[countries['year'] == 1952]
print(c_1952.head())
c_2007 = countries.loc[countries['year'] == 2007]
print(c_2007.head())
print(type(c_1952))
c_merge = c_1952.merge(c_2007, left_on = 'country', right_on = 'country')
print(c_merge.head())
c_merge.drop(['year_x', 'year_y'], axis = 1)
print(c_merge.head())
c_merge['population_growth'] = c_merge['population_y'] - c_merge['population_x']
print(c_merge.head())
print(c_merge.shape)
print(type(c_merge))
c_merge = c_merge.sort_values('population_growth', ascending = False).head(10)
print(c_merge.head(10))
names = ['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangledesh', 
'Nigeria', 'Mexico', 'Phillipines']
pop_grow = (c_merge['population_growth']/10**6)
plt.figure(figure_size = (15,9))
plt.bar(names, pop_grow, width = (0.6))
plt.xlabel('country')
plt.title('Top 10 countries with the biggest population growth from 1952 to 2007')
plt.xticks(rotation = 45)
for x,y in zip(names, pop_grow):
    label = "({:.2f})".format(y)
    plt.annotate(label,(x,y), textcoords= 'offset_points', xy_text = (0,10), ha = 'center')
plt.show()