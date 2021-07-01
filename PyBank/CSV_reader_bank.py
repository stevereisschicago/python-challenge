#CSV_Reader_Bank

#print out the file with context
import csv
with open ("budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
   
    line_count = 0
    for row in csv_reader:
        print (f"{row[0]} is the date and {row[1]} is the profit or loss")  

#print out the total number of records
file = open("budget_data.csv")
reader = csv. reader(file)
total_months= len(list(reader)) - 1
print(total_months)      


# #print out the sum of the profit/loss
# total_dollars = 0
# for row[1] in open("budget_data.csv"):
#     row[1] = float(row[1])
#   	total_dollars = total_dollars += row[1]
# print(total_dollars "is the total")

#open ("budget_data.csv") as csv_file:
#csv_file = csv.reader(open("budget.data.csv"))
#dist = 0
#for row in csv_file:
 #   _dist = row[1]
  #  try:
   #     _dist = float(_dist)
    #except ValueError:
     #   _dist = 0
    #dist += _dist
#print(dist)