"""

"""
import pandas as pd
import matplotlib.pyplot as plt

#### Print Header ####
print('**************************************')
print('Food Price Variations')
print('**************************************')


#### Read data from file ####
file_data = pd.read_csv("wfp_food_prices_Sri-lanka.csv")

#print(file_data.head())
print(file_data.head())

#### Remove the first row since it contain irrelevant values ####
file_data = file_data.drop(file_data.index[0])

#### Filter the commodities and markets you want ####
#### You can change the values here to pick any commodity or market ####
commodity = file_data[file_data.cmname.str.contains('Sugar - Retail')]
commodity = commodity[commodity.mktname == 'Kalutara']

#### Display the top 5 rows of the filtered commodity data ####
print(commodity.head())

#### Print the length of the filtered data we have now ####
print(len(commodity))

#### Start plotting the graph ####
plt.figure()
x = commodity.date
y = commodity.price

plt.bar(x, y)
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Price')
plt.title('Price Variations of Commodities')

plt.show()

