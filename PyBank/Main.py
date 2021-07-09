#BankTest.py
import csv
import os

#NOTE: need to be in Pybank file on terminal command line
budget_data = os.path.join(".", "Resources-Bank", "budget_data.csv")

#-------------------------
#Print Header
print("Financial Analysis")
print ("-----------------------")
#---------------------------


#-------------------
#print out the file with context - this is not required, just for reference
import csv
with open ("budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    line_count = 0
    for row in csv_reader:
        print (f"{row[0]} is the date and {row[1]} is the profit or loss")  
#--------------


#-------------
#print out the total number of records
file = open("budget_data.csv")
reader = csv. reader(file)
total_months= len(list(reader))
total_months = total_months - 1
print("Total Months: " + str(total_months))   
#--------------


#-------------
#print out the total
with open ("budget_data.csv") as csv_file:
    file = csv.reader(open("budget_data.csv"))
    next(file)
    total = 0
    for row in file:
        total += float(row[1])
        total1 = "${:,.2f}".format(total)
print ("Total: " + str(total1)) 
#--------------------


#-------------
#Average Profit and Loss
import csv
with open ("budget_data.csv", 'r') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=",")
    next(csv_data)

    difference = []
    month = []
    past = 0
    for value in csv_data:
        if past != 0:
	        difference.append(int(value[1]) - int(past))
        month.append(value[0])
        past = value[1]


average = (sum(difference)/len(difference))
average1 = "${:,.2f}".format(average)
print ("Average Change: " + str(average1))
#----------------


#---------
#print out the highest change 
highest = max(difference) 
index = difference.index(highest)
target_month = month[index + 1]
#print(target_month)
highest2 = "${:,.2f}".format(highest)
print (f"Greatest Increase in Profits: " + target_month + "  " + highest2)
#------------


#------------
#print out the lowest change  
lowest = min(difference)
index2 = difference.index(lowest)
target_month2 = month[index2 + 1]
lowest2 = "${:,.2f}".format(lowest)
print (f"Greatest Decrease in Profits: " + target_month2 + "  " + lowest2) 

#-----------------------


#-----------------------
#write to a text file 
with open('readme.txt', 'w') as f:
    f.write("Financial Analysis")
    f.write("\n")
    f.write("---------------------")
    f.write("\n")
    f.write("Total Months: " + str(total_months))  
    f.write("\n")
    f.write("Total: " + str(total1))
    f.write("\n")
    f.write("Average Change: " + str(average1))
    f.write("\n")
    f.write("Greatest Increase in Profits: " + target_month + "  " + str(highest2)) 
    f.write("\n")
    f.write("Greatest Decrease in Profits: " + target_month2 + "  " + str(lowest2)) 