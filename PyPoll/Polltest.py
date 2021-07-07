#tpolltest.py
#3million lines, smaller file to test

import csv
import os

#Headers
print("Election Results")
print("----------------------")


#Total number of rows / votes
with open ("election_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = len(list(csv_reader)) - 1
    print(f"Total Votes: " + str(line_count))
  print("----------------------")

  
#candidates with name, percentage, # of votes


#winner
#Print(f"Winner: " + unnamed variable)

print("hello everyone")