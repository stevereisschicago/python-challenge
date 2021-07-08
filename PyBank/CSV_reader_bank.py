# #CSV_Reader_Bank


#-------------------------
#Print Header
print("Financial Analysis")
print ("-----------------------")
#---------------------------


#-------------------
#print out the file with context - not required
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
print("Total months: " + str(total_months))   
#--------------


#-------------
#print out the total
with open ("budget_data.csv") as csv_file:
    file = csv.reader(open("budget_data.csv"))
    next(file)
    total = 0
    for row in file:
        total += float(row[1])
        #format the outcome as currency
print ("Total: " + str(total)) 
#--------------------

#-------------
#Average Profit and Loss
import csv
with open ("budget_data.csv", 'r') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=",")
    next(csv_data)

    difference = []
    #past = None
    past = 0
    for value in csv_data:
	    #if past is not None:
        if past != 0:
	        difference.append(int(value[1]) - int(past))
        past = value[1]

print (sum(difference)/len(difference))
#----------------


#---------
#print out the highest change but doesn't have the month 
highest = max(difference) 
highest2 = "${:,.2f}".format(highest)
print (f"Greatest Increase in Profits: " + highest2)
#maxpos = difference.index(highest)
#maxpos2 = maxpos + 1
#print(maxpos2)
#------------


#------------
#print out the lowest change but doesn't have the month 
lowest = min(difference)
lowest2 = "${:,.2f}".format(lowest)
print (f"Greatest Decrease in Profits: " + lowest2) 
#minpos = difference.index(lowest)
#minpos1 = minpos + 1
#print(minpos1)
#-----------------------


#-----------------------
#write to a text tile but doesn't have the months 
with open('readme.txt', 'w') as f:
    f.write("Financial Analysis")
    f.write("\n")
    f.write("---------------------")
    f.write("\n")
    f.write("Total months: " + str(total_months))  
    f.write("\n")
    f.write("Total: " + str(total1))
    f.write("\n")
    f.write("Average change: " + str(averagechange2))
    f.write("\n")
    f.write("Greatest increase in profits: " + str(highest2)) # need to add date
    f.write("\n")
    f.write("Greatest decrease in profits: " + str(lowest2)) #need to add date