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

for row in climatedata:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])
# fetch data...

plt.plot()
plt.subplot(2, 1, 1)
# 2 rows, 1 column, 1st plot
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 
plt.show()



