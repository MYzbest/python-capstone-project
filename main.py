# with open("50_states.csv") as data_file:
#     data_file
 
import pandas
# with open("50_states.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)
 
# data = pandas.read_csv("50_states.csv")
# print(data["state"])
title = "004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv"
data = pandas.read_csv("004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_len = len(data[data["Primary Fur Color"] == "Gray"])
red_len = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_len = len(data[data["Primary Fur Color"] == "Black"])
dic = {
    "Fur Color":["Gray" , "Cinnamon" , "Black"],
    "Count":[gray_len , red_len , black_len]

}
df = pandas.DataFrame(dic)
df.to_csv("copy.csv")
