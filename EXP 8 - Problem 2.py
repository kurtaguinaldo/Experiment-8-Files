import pandas as pd

cars = pd.read_csv('cars.csv')

print(cars.iloc[0:5,1::2])

print(cars[cars['Model'] == "Mazda RX4"])

print(cars.loc[cars['Model'] == "Camaro Z28",['Model','cyl']])

x = cars.loc[cars['Model'] == "Mazda RX4 Wag",['Model','cyl','gear']]
y = cars.loc[cars['Model'] == "Honda Civic",['Model','cyl','gear']]
z = cars.loc[cars['Model'] == "Ford Pantera L",['Model','cyl','gear']]

w = x.append(y)
v = w.append(z)

print(v)