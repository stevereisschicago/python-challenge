#tpolltest.py
#3million lines, smaller file to test

import csv
import os

#need to be in Pypoll file on terminal command line
election_data = os.path.join(".", "Resources-Poll", "election_data.csv")
#--------------------


#--------------------
#Headers
print("Election Results")
print("----------------------")
#---------------------


#--------------------
#Total number of rows / votes
with open ("election_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    total_votes = len(list(csv_reader)) - 1
    print(f"Total Votes: " + str(total_votes))
print("----------------------")
#---------------------
  

#---------------------  
with open ("election_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
   
    khanvotes = 0
    correyvotes = 0
    livotes = 0
    otooleyvotes = 0 

    for row in csv_reader:  
        if row[2] == "Khan":
            khanvotes = khanvotes + 1
        elif row[2] == "Correy":
            correyvotes = correyvotes + 1
        elif row[2] == "Li":
           livotes = livotes + 1
        elif row[2] == "O'Tooley":
           otooleyvotes = otooleyvotes + 1

#print("Khan: " + str(khanvotes))
#print("Correy: " + str(correyvotes))
#print("Li: " + str(livotes))
#print("O'Tooley: " + str(otooleyvotes))

khanpercent = int(khanvotes) / int(total_votes)
correypercent = int(correyvotes) / int(total_votes)
lipercent = int(livotes) / int(total_votes)
otooleypercent = int(otooleyvotes) / int(total_votes)

khanpercent2 = '{0:.2f}'.format(khanpercent * 100)
correypercent2 = '{0:.2f}'.format(correypercent * 100)
lipercent2 = '{0:.2f}'.format(lipercent * 100)
otooleypercent2 = '{0:.2f}'.format(otooleypercent * 100)
#print(khanpercent2)
#print(correypercent)
#print(lipercent)
#print(otooleypercent)

print(f"Khan: {khanpercent2}% {khanvotes}")
print(f"Correy: {correypercent2}% {correyvotes}")
print(f"Li: {lipercent2}% {livotes}")
print(f"O'Tooley: {otooleypercent2}% {otooleyvotes}")


    # #make more elegant, put into a dictionary


print("---------------------")


#winner listing 
if khanvotes > correyvotes and livotes and otooleyvotes:
    winner = "Khan"
elif correyvotes > khanvotes and livotes and otooleyvotes:
    winner = "Correy"
elif livotes > khanvotes and correyvotes and otooleyvotes:
    winner = "Li"
else:
    winner = "O'Toole"
print("Winner: " + (winner))


print("---------------------")


#write to a text tile need to fill out 
with open('readme.txt', 'w') as f:
    f.write("Election Results")
    f.write("\n")
    f.write("---------------------")
    f.write("\n")
    f.write("Total Votes: " + str(total_votes))  
    f.write("\n")
    f.write("---------------------")
    f.write("\n")
    f.write(f"Khan: {khanpercent2}% {khanvotes}")
    f.write("\n")
    f.write(f"Correy: {correypercent2}% {correyvotes}")
    f.write("\n")
    f.write(f"Li: {lipercent2}% {livotes}")
    f.write("\n")
    f.write(f"O'Tooley: {otooleypercent2}% {otooleyvotes}")
    f.write("\n")
    f.write("---------------------")
    f.write("\n")
    f.write("Winner: " + (winner))
    f.write("\n")
    f.write("---------------------")