#!/usr/bin/python3

import sys
import csv
import math
import random
import datetime
import unicodedata

#line_end="\n\r" # Serial
line_end="\r\n" # LPT
feed_count=3
space="                                        "

print_test=False

# Print to real printer
def lprint(line):
    with open('/dev/lp0', 'w') as printer:
                printer.write(line)


print("Physical Hardcopy Supporter Label Generator")
return_address="Name"+line_end+"Street"+line_end+"City, State Zip" # Fill this in !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
               
def simplify(text):
    return str(unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode())

supporters = []

# Add Permanent supports to files to read
sys.argv.append("perm.csv")

with open(sys.argv[1]) as csv_in:
    print("Reading: " + str(sys.argv[1]))
    csv_parsed = csv.DictReader(csv_in, delimiter=",")
    for row in csv_parsed:
        print("Generating Label For:")

        print(str(row['Addressee']))
        print(str(row['Street']))
        print(str(row['City'])+", "+simplify(row['State'])+" "+simplify(row['Zip']))
        print(str(row['Country']))
        print("")
        print("as")
        print("")
        print(simplify(row['Addressee']))
        print(simplify(row['Street']))
        print(simplify(row['City'])+", "+simplify(row['State'])+" "+simplify(row['Zip']))
        print(simplify(row['Country']))
        
        result=input("Print? (Y/n/s)")
        print(result)
        if result.strip() == "n":
            print("QUIT")
            sys.exit()
        if result.strip() == "s":
            print("SKIP")
            continue
        
        
        if str(row['Addressee']) == "":
            print("NO ADDRESS!!!!")
            print(row)
        else:
            for i in range(1,feed_count):
                print(line_end)
                
            out=lprint
            if print_test:
                out=print

            hr="-"
            print(hr.rjust(80,"-"))

            out(return_address)
            out(line_end)
            out(line_end)
            out(line_end)
            out(line_end)
            out(line_end)
            out(line_end)
            out(space+simplify(row['Addressee']))
            out(line_end)
            out(space+simplify(row['Street']))
            out(line_end)
            out(space+simplify(row['City'])+", "+simplify(row['State'])+" "+simplify(row['Zip']))
            out(line_end)
            out(space+simplify(row['Country']))
            out(line_end)
                
            hr="-"
            print(hr.rjust(80,"-"))

        input("Press Enter to continue...")
