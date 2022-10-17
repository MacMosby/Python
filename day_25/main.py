# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
#
# data = pandas.read_csv("weather_data.csv")
#
# hottest_day = data[data.temp == data.temp.max()]
# print(hottest_day)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
num_of_cinnamons = len(data[data["Primary Fur Color"] == "Cinnamon"])
num_of_gray = len(data[data["Primary Fur Color"] == "Gray"])
num_of_blacks = len(data[data["Primary Fur Color"] == "Black"])

print(num_of_gray)
print(num_of_cinnamons)
print(num_of_blacks)


data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [num_of_gray, num_of_cinnamons, num_of_blacks]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
