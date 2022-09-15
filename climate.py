import matplotlib.pyplot as plt

import sqlite3

connection = sqlite3.connect("climate.db")
cursor = connection.cursor()
cursor.execute("SELECT * from ClimateData")
# do a SQL command
climatedata = cursor.fetchall()
# get those data....
years = []
co2 = []
temp = []

import pandas as pd

climate = pd.read_csv("climate.csv")
years = climate['Year'].to_numpy()
co2 = climate['CO2'].to_numpy()
temp = climate['Temperature'].to_numpy()


for row in climatedata:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])
# fetch data...

plt.plot()
plt.subplot(2, 1, 1)

# 2 rows, 1 column, 1st plot
plt.plot(years, co2, 'b--') 

plot(years, co2, 'b--') 

plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 
plt.show()

plt.subplot(2, 1, 2)
plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp.png") 

