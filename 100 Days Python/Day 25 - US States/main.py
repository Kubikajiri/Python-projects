import csv
# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	temperatures = []
# 	for row in data:
# 		if row[1] != 'temp':
# 			temperatures.append(int(row[1]))
# 	print(temperatures)
# 	print(data)

import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data['temp'].to_list()

sum_temp = 0
for n in range(0, len(temp_list)):
	sum_temp += temp_list[n]
	avg = sum_temp/len(temp_list)

# instead, there is a function SUM (i forgot about it lol)
average = sum(temp_list)/len(temp_list)


# another option is a simple Pandas method

print(data['temp'].mean())

print(data['temp'].max())

print(data[data.temp == data.temp.max()])


# Create a datafame from scratch

data_dict = {
	"students": ["Amy", "Bruce", "Brian", "Lilly"],
	"marks": [76, 73, 59, 29]
}
pandas.DataFrame(data_dict)