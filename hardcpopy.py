#!/usr/bin/python3

import sys
import csv
import math
import random
import datetime
import unicodedata

print("Hardcopy Supporter Printout Generator")

def name_sub(row):
    
    if len(row) == 1:
        print("No email, adding "+row[0])
        return row[0]
    
    with open("name_sub.csv") as csv_in:
        csv_parsed = csv.reader(csv_in, delimiter=",")
        notsubbed=True
        for row_subs in csv_parsed:
            if row[1] == row_subs[0]:
                notsubbed=False
                print("subbing, adding "+row[0])
                return row_subs[1]
                print("Substituting [" + str(row[0]) + "] for [" + row_subs[1] + "]")
        if notsubbed:
            print("No sub, adding "+row[0])
            return row[0]
                
def simplify(text):
    return str(unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode())

pagelen=80
cols=3
collen=math.floor(pagelen/cols)
#line_end="\n\r" # Serial
line_end="\r\n" # LPT

if len(sys.argv) < 3:
    print("Must include both CSV files for Patreon on Youtube Members")
    sys.exit()

print("")
print("Using: " + str(sys.argv[1]) + " and " + str(sys.argv[2]))
print("")
supporters = []

# Add Permanent supports to files to read
sys.argv.append("perm.csv")

for arg in range(1,(len(sys.argv))):
    with open(sys.argv[arg]) as csv_in:
        print("Reading: " + str(sys.argv[arg]))
        csv_parsed = csv.reader(csv_in, delimiter=",")
        headers = next(csv_parsed, None)
        for row in csv_parsed:
            supporters.append(name_sub(row))

# Randomize name list
random.shuffle(supporters)


hr="="
hr=hr.rjust(pagelen,"=")

p = open("printout.txt","w")
p.write(" -- Tech Tangents Hardcopy Supporters! -- ".center(pagelen)+line_end)
p.write(datetime.datetime.now().strftime("%B, %Y").center(pagelen)+line_end)
p.write(hr)
p.write(line_end)

for i in range(len(supporters)):
    p.write(simplify(supporters[i].ljust(collen)[0:collen]))
    if (i+1) % cols == 0:
        p.write(line_end)
    else:
        p.write(" ")

p.write(line_end)
p.write(line_end)
p.write(line_end)
p.write(line_end)
p.write(line_end)
p.write(line_end)
p.close()

print("Printout file generated for " + str(len(supporters)) + " supporters")
