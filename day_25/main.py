import pandas as pd


# data = pandas.read_csv('weather_data.csv')

data = pd.read_csv("Squirrel_Data.csv")
color = data['Primary Fur Color'].value_counts()
print(color.name)

# data.dic = {
#     "Fur Color" :
# }
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
#
# print(data["temp"].mean())
# print(data["temp"].mode())
# print(data["temp"].median())
# print(data["temp"].max())
#
#
# print(data.day)
#
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)
# celsius = monday.temp
# fer = (celsius * 9/5) + 32
# print(fer)