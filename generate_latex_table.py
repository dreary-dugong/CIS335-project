#!/bin/python3
#generate_latex_table.py
#generate a latex formatted table from lines of a file given certain parameters
#Daniel Gysi
#CIS-335
#December 6, 2021

from sys import argv
from sys import stdout
import math

def latexify(s):
    """replace characters in string with latex escape sequences"""
    #tfw i thought this script would be easy
    #it's even more fun because of python's own escape sequences
    s = s.replace("\n", "")
    s = s.replace("$", "\\$")
    s = s.replace("#", "\\#")
    s = s.replace("%", "\\%")
    s = s.replace("&", "\\&")
    return s

def main():
    infile = argv[1]
    columns = int(argv[2]) if len(argv) >= 3 else 3
    
    #begin table, define columns
    out = ""
    out += "\\begin{center}\n"
    out += "\\begin{tabular}{|"
    for _ in range(columns):
        out += "c|"
    out += "}\n"

    out += "\\hline\n"

    #put in lines of file
    with open(infile) as f:
        lines = f.readlines()

    #we want to fit all the entries on the page
    #(if possible) so we need the big ones in
    #the same column and the small ones in
    #the same column
    #this is a pain in the ass.
    #hahahahahahhahahahahhahahahahha
    #it gets worse. Some letters are bigger
    #than other letters. I'm not gonna go
    #that far but that would be the next step
    entries = sorted(lines, key=len)
    newentries = [] 
    divisor = math.ceil(len(entries)/columns)
    for i in range(divisor):
        for j in range(len(entries)):
            if j % divisor == i:
                newentries.append(entries[j])
    entries = newentries

        

        
    

    column = 0 #what column are we currently on
    for entry in entries:
        #add items to table
        entry = latexify(entry) 
        if column == 0:
            out += entry
        else:
            out += " & " + entry
        #if we hit the last column, go to the next line
        if column == columns - 1:
            out += " \\\\\n\\hline\n"
            column = 0
        else:
            column += 1

    #close table if it doesn't divide evenly
    if column != 0:
        out += " \\\\\n\\hline\n"

    out += "\\end{tabular}\n"
    out += "\\end{center}"
    
    stdout.write(out)



if __name__ == "__main__":
    main()
