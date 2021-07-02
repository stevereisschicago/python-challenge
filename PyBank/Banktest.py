#BankTest.py
import csv
import os

#open.path.join("desktop/python-challenge/pybank/budget_data.csv") - NOT WORKING 

#print out the file with context - not required
with open ("budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
   
    line_count = 0
    for row in csv_reader:
        print (f"{row[0]} is the date and {row[1]} is the profit or loss")  


#print out the total number of records
file = open("budget_data.csv")
reader = csv. reader(file)
total_months= len(list(reader)) - 1
print("Total months: " + str(total_months))    


#print out the total
with open ("budget_data.csv") as csv_file:
    csv_file = csv.reader(open("budget_data.csv"))
    next(csv_file)
    total = 0
    for row in csv_file:
        total += float(row[1])
print ("Total: " + str(total)) 

#Average Profit and Loss
import csv
with open ("budget_data.csv", 'r') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=",")
    next(csv_data)

    difference = []
    print(difference) 
    #past = None
    past = 0
    for value in csv_data:
	    #if past is not None:
        if past != 0:
	        difference.append(int(value[1]) - int(past))
        past = value[1]

print (sum(difference)/len(difference))