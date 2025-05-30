#!/data/programs/bin/python3

"""
SNPCounter.py v0.7

Author:
Pavel Salazar-Fernandez
April 2016
epsalazarf@gmail.com
LANGEBIO, Mexico

Developed in:
Python 3.5.1
Anaconda 2.5.0 (64-bit)
Spyder 2.3.8 (64-bit, Windows)

Function:
Counts the number of SNPs per Mb from a BIM file and output a CSV

Requirements:
- Python 3+ or better (Download at http://www.python.org/)
- Incompatible with Python 2.7+

Usage:
- Copy the script file to desired location.
- Run the following command:

python SNPCounter.py [file.bim]

"""

#<START>
#Load required module
import sys,csv
from itertools import chain

#Variables

filename = sys.argv[1]
lnread = 0
chcksum = 0
chrm = 1
wndwbegin = 0
wndwend = 999999
snpcount = 0
snppchr = 0

#CORE
if filename.endswith(".bim") or filename.endswith(".pvar"):
    print ("Processing " + filename)
    print ("Chromosome " + str(chrm) + "...")
    newfile = (filename[:-3] + "snpcounts.txt")
    with open(filename, 'r') as f:
        with open(newfile, 'w',newline='') as fout:
            OUT = csv.writer(fout, delimiter= ' ', lineterminator="\n")
            for line in f:
                lnread += 1
                columns = line.split()
                if (int(columns[0]) == chrm):
                    if int(columns[1]) < wndwend:
                        snpcount += 1
                    else:
                        OUT.writerow([("hs"+str(chrm)),wndwbegin,wndwend,snpcount])
                        chcksum += snpcount
                        snppchr += snpcount
                        snpcount = 0
                        wndwbegin += 1000000
                        wndwend += 1000000
                        while (int(columns[1]) > wndwend):                    
                            OUT.writerow([("hs"+str(chrm)),wndwbegin,wndwend,snpcount])
                            chcksum += snpcount                        
                            wndwbegin += 1000000
                            wndwend += 1000000
                        snpcount += 1
                else:             
                    OUT.writerow([("hs"+str(chrm)),wndwbegin,wndwend,snpcount])
                    chcksum += snpcount
                    snppchr += snpcount
                    print ("Found " + str(snppchr) + " SNPs")                
                    chrm += 1
                    print ("Chromosome " + str(chrm) + "...")                    
                    snpcount = 0
                    snppchr = 0
                    wndwbegin = 0
                    wndwend = 999999
                    while (int(columns[0]) > chrm):
                        print ("Found " + str(snppchr) + " SNPs (omitted)")                        
                        chrm += 1
                        print ("Chromosome " + str(chrm) + "...")
                    while (int(columns[1]) > wndwend):                    
                        OUT.writerow([("hs"+str(chrm)),wndwbegin,wndwend,snpcount])
                        chcksum += snpcount                        
                        wndwbegin += 1000000
                        wndwend += 1000000
                    snpcount += 1
            OUT.writerow([("hs"+str(chrm)),wndwbegin,wndwend,snpcount])
            chcksum += snpcount
            snppchr += snpcount
            print ("Found " + str(snppchr) + " SNPs")
            print ("Success! Counting finished")
            print (" - Lines read:   " + str(lnread))
            print (" - SNPs counted: " + str(chcksum))
        print (" > Output file: "+ newfile)
else:
    print ("ERROR: Not a BIM/MAP or PVAR file")


#<END>
