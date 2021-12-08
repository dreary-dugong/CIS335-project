#changehash.py
#take a file with passwords and hashes and output a new file with
#the same passwords hashed in md5 instead
#Daniel Gysi
#CIS-335
#November 28, 2021

from passlib import hash as plhash 
def main():
    #if i cared more I could get args from stdin
    inputfile = input("Enter the input filename: ")
    outputfile = input("Enter the output file name: ")
    pws = []

    #read passwords from input
    with open(inputfile) as f:
        for line in f:
            pws.append(line.split(",")[0]) #would regex be more intuitive?

    #rehash and save to output
    with open(outputfile, "w") as f:
        for pw in pws:
            h = plhash.md5_crypt.hash(pw)
            f.writelines(pw + "," + h+"\n") #I should use fstrings if I cared more

    print("Passwords rehashed.")

if __name__ == "__main__":
    main()
