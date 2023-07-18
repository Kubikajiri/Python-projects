import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

data_dict = data.to_dict()

grouped = data.groupby(data['Primary Fur Color']).count()


print(grouped["Unique Squirrel ID"])


