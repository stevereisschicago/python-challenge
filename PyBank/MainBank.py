#BankTest.py
import csv
import os

#budget_data = os.path.join("..", "PyBank", "budget_data.csv")
# #print out the file with context - not required
# with open ("budget_data.csv") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     line_count = 0
#     for row in csv_reader:
#         print (f"{row[0]} is the date and {row[1]} is the profit or loss")  


#-------------------------
#Print Header
print("Financial Analysis")
print ("-----------------------")
#---------------------------


#----------------------------
#print out the total number of records
file = open("budget_data.csv")
reader = csv. reader(file)
total_months= len(list(reader))
total_months = total_months - 1
print("Total months: " + str(total_months))    
#--------------------------


#--------------------------
#print out the total
with open ("budget_data.csv") as csv_file:
    csv_file = csv.reader(open("budget_data.csv"))
    next(csv_file)
    total = 0
    for row in csv_file:
        total += float(row[1])
        total1 = "${:,.2f}".format(total)  
    print (f"Total: " + total1) 
#-------------------------


# #----------------------
#Average Profit and Loss
import csv
with open ("budget_data.csv", 'r') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=",")
    next(csv_data)

    difference = []
    months = []
    past = 0
    past2 = 0
    monthnum = None
    for value in csv_data:
	    #if past is not None:
        if past != 0:
	        difference.append(int(value[1]) - int(past))
        past = value[1]    
    for value in csv_data:
        if past2 != 0:
            months.append(int(monthnum[0]) + 1)
        months = value[0]
averagechange = (sum(difference)/len(difference))    
averagechange2 = "${:,.2f}".format(averagechange)  
print (f"Average change: " + averagechange2) 
#print (sum(difference)/len(difference)) # or could print averagechange
#-----------------------
import csv
with open ("budget_data.csv", 'r') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=",")
    next(csv_data)

    dirdiff = {"month":[],"change":[]}
    past = 0

    for value in csv_data:
        #if past is not None:
        if past != 0:
           value = int(value[1]) - int(past)
           dirdiff["month"].append(value[0])
           dirdiff["change"].append(value[1])
        past = value[1]
#   #'s are wrong, suddenly can't populate the dirdiff directory
print(dirdiff)


#-------------------------
#print out the highest change but doesn't have the month 
with open ("budget_data.csv") as csv_file:
    file1 = csv.reader(open("budget_data.csv"))
    next(file1)
highest = max(difference) 
highest2 = "${:,.2f}".format(highest)
print (f"Greatest Increase in Profits: " + highest2)

#https://www.kite.com/python/answers/how-to-search-if-dictionary-value-contains-certain-string-in-python
# highest3 = []
# for highest3 in dirdiff.values():
#     if highest in highest3:
#         highest3.append()
# print(values)

print(list(dirdiff.keys())[list(dirdiff.values()).index("1605228")]) # highest?

#---------------------
# for dirdiff["change"]:
    # if highest == dirdiff["change"]:
    # print (f"Greatest increase in profits: " + {dirdiff})

# averagechange = (sum(difference)/len(difference))    
# averagechange2 = "${:,.2f}".format(averagechange)  
# print (f"Average change: " + averagechange2) 
#print (sum(difference)/len(difference)) # or could print averagechange

#----------------------
#print out the highest change but doesn't have the month 
with open ("budget_data.csv") as csv_file:
    file1 = csv.reader(open("budget_data.csv"))
    next(file1)
highest = max(difference) 
highest2 = "${:,.2f}".format(highest)
# print (f"Greatest Increase in Profits: " + highest2)
# maxpos = difference.index(highest)
# maxpos2 = maxpos + 1
# print(maxpos2)
# #print(months[maxpos2])

# # with open ("budget_data.csv") as csv_file:
# #     csv_reader = csv.reader(csv_file, delimiter=",")
# #     #next (csv_data)
# #     for row in csv_reader:
# #         row = maxpos2
# #         #linecount = maxpos + 1
# #         #if row[0] == maxpos2:
# #             #return csv_reader.line_num
# #             #print(csv_reader.line_num)
# #         print (f"{row[0]} is the date") 
# #         break
# #     #for row in file1:
# # 	    #if highest == int(row[1]):
# # 	 	    #print(f"{row[0]} {row[1]}")
# # 	 	    #break

# # # #print out the month and the highest
# # #with open ("budget_data.csv") as csv_file:
# #     #csv_reader = csv.reader(csv_file, delimiter=",")
# #     #for row in csv_reader:
# #      #   print (f"{row[maxpos]} is the month") 


# #-----------------------
# #print out the lowest change but doesn't have the month 
# lowest = min(difference)
# lowest2 = "${:,.2f}".format(lowest)
# print (f"Greatest Decrease in Profits: " + lowest2) 
# minpos = difference.index(lowest)
# minpos1 = minpos + 1
# print(minpos1)
# #-----------------------


# #-----------------------
# #write to a text tile but doesn't have the months 
# with open('readme.txt', 'w') as f:
#     f.write("Financial Analysis")
#     f.write("\n")
#     f.write("---------------------")
#     f.write("\n")
#     f.write("Total months: " + str(total_months))  
#     f.write("\n")
#     f.write("Total: " + str(total1))
#     f.write("\n")
#     f.write("Average change: " + str(averagechange2))
#     f.write("\n")
#     f.write("Greatest increase in profits: " + str(highest2)) # need to add date
#     f.write("\n")
#     f.write("Greatest decrease in profits: " + str(lowest2)) #need to add date
# #-----------------------------