#hash_compare.py
#compare the time it takes to hash passowrds with
#various hashing schemes
#Daniel Gysi
#CIS-335
#November 14, 2021

import math
import time
from passlib import pwd
from passlib import hash as plhash

def main():
    output_file = "hashes_compared.csv"
    n = 10_000 #how many times we test each hash
            #note that as n increases, size of the pws increases

    #hash methods to test
    hashes = [plhash.argon2, plhash.bcrypt,
            plhash.sha256_crypt, plhash.md5_crypt,
            plhash.sha1_crypt]

    #write file header
    with open(output_file, "w") as f:
        columns = "Password"
        for h in hashes:
            columns += "," + h.__name__
        columns = columns + "\n"
        f.writelines(columns)
    
    lines = [] 
    for i in range(1, n+1): #start at 1 to deal with the logarithm
        
        #passwords get longer over time
        #in hindsight, this was a bad way to do this
        pw = ""
        for j in range(int(math.log(i, 10))+1):
            pw = pw + pwd.genword()
        line = pw

        #record the time for each hash
        for h in hashes:
            start = time.time()
            v = h.hash(pw)
            end = time.time()
            elapsed = end - start
            line = line + "," + str(elapsed) 
        line += "\n"
        lines.append(line)

        #write in chunks
        if len(lines) == n//10:
            with open(output_file, "a") as f:
                f.writelines(lines)
            lines = []

        #progress update
        if i % 50 == 0:
            print("Hashed " + str(i) + " passwords so far.")


if __name__ == "__main__":
    main()

