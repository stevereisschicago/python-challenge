#tpolltest2.py
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
    #break

#print("Khan: " + str(khanvotes))
#print("Correy: " + str(correyvotes))
#print("Li: " + str(livotes))
#print("O'Tooley: " + str(otooleyvotes))

#----------Everything above WAS working-------------
   
khanpercent = int(khanvotes) / int(total_votes)
correypercent = int(correyvotes) / int(total_votes)
lipercent = int(livotes) / int(total_votes)
otooleypercent = int(otooleyvotes) / int(total_votes)

#print(khanpercent)
#print(correypercent)
#print(lipercent)
#print(otooleypercent)



#kahnpercent1 = "{:.2%}".format(khanpercent)

print(f"Khan: {khanpercent} {khanvotes}")
print(f"Correy: {correypercent} {correyvotes}")
print(f"Li: {lipercent} {livotes}")
print(f"O'Tooley: {otooleypercent} {otooleyvotes}")




#print(kahnpercent1)


    # #tranfer kahnpercent into percentage
    # #make more elegant, put into a dictionary

   # print(f"Kahn: {kahnpercent} {khanvotes}")

print("---------------------")


#winner listing 
#if kahnvotes > correyvotes and livotes and otooley votes
#     winner = "Khan"
#     Print("Winner: Khan")
# elif 

#Print(f"Winner: {winner}"")
#print("---------------------")


#-----------------------
#write to a text tile need to fill out 
# with open('readme.txt', 'w') as f:
#     f.write("Election Results")
#     f.write("\n")
#     f.write("---------------------")
#     f.write("\n")
#     f.write("Total Votes: " + str(total_votes))  
#     f.write("\n")
#     f.write("---------------------")
#     f.write("Khan: " + )
#     f.write("\n")
#     f.write("Correy: " + )
#     f.write("\n")
#     f.write("Li: " + )
#     f.write("\n")
#     f.write("O'Tooley: " + )
#     f.write(f"Winner: {winner}")