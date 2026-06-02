# with open("weather_data.csv") as file:
#     content = file.readlines()
#     print(content)

import csv

# with open("weather_data.csv") as file:
#     content = csv.reader(file)

#     temps = []
#     for row in content:
#         if row[1] != "temp":
#             temps.append(int(row[1]))

#     print(temps)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])