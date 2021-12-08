def main():

    argon = []
    bcrypt = []
    sha256 =[]
    md5 =[]
    sha1 =[]

    with open("hashes_compared.csv") as f:
        f.readline()
        for line in f:
            _, arg, bc, sha25, md, sha = line.split(",")
            argon.append(float(arg))
            bcrypt.append(float(bc))
            sha256.append(float(sha25))
            md5.append(float(md))
            sha1.append(float(sha))

    print(f"Argon2 average: {sum(argon)/len(argon)}")
    print(f"Bcrypt average: {sum(bcrypt)/len(bcrypt)}")
    print(f"SHA-256 average: {sum(sha256)/len(sha256)}")
    print(f"MD5 average: {sum(md5)/len(md5)}")
    print(f"SHA-1 average: {sum(sha1)/len(sha1)}")

if __name__ == "__main__":
    main()
    


