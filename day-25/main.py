# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(data)

data_dict = data.to_dict()
#print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())

print(data["temp"].max())

#Get data in columns
print(data["condition"])
print(data.condition)

#Get data in row
print(data[data.day == "Monday"])