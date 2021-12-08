#hashing.py
#prompt the user for passwords following various rules then hash them and store them
#Daniel Gysi
#CIS-335
#November 7, 2021

import bcrypt #NOTE: this is py-bcrypt, not bcrypt. bcrypt has different syntax
from passlib.hash import pbkdf2_sha256

def main():
    bcryptBasic8File = "bcrypt-basic8.txt"
    bcryptComp8File = "bcrypt-comp8.txt"
    bcryptBasic16File = "bcrypt-basic16.txt"
    pbkBasic8File = "pbk-basic8.txt"
    pbkComp8File = "pbk-comp8.txt"
    pbkBasic16File = "pbk-basic16.txt"

    print("""Password Types: \n
          1: basic 8 (any 8 ascii characters)
          2: comprehensive 8 (8 characters, one number, one lowercase letter, 
            one capital letter, one special character)
          3: basic 16 (any 16 ascii characters)
        """)
    choice = input("Choose which password type to enter: ")

    validationFuncs = {1: validate_basic_8, 2: validate_comp_8,
            3: validate_basic_16}
    outputFiles = {1:(bcryptBasic8File, pbkBasic8File),
            2: (bcryptComp8File, pbkComp8File),
            3: (bcryptBasic16File, pbkBasic16File)}

    validationFunc = validationFuncs[int(choice)]
    outputs = outputFiles[int(choice)]
    bcryptOutput, pbkOutput = outputs
    
    passwordsEntered = get_passwords(bcryptOutput)
    print(str(len(passwordsEntered)) + " passwords already stored.")

    while True:
        password = input("\nEnter a password (-1 to quit): ")
        if password in {"-1", "exit"}:
            break
        if not validationFunc(password)[0]:
            print(validationFunc(password)[1])
        elif password in passwordsEntered:
            print("You've entered this password already!")
        else:
            passwordsEntered.add(password)
            write_output(get_bcrypt_line(password), bcryptOutput)
            write_output(get_pbk_line(password), pbkOutput)
            print("Password salted, hashed, and stored successfully.")
            print(str(len(passwordsEntered)) + " passwords stored so far.")

    print("Password entry terminated.")


def validate_basic_8(s):
    if len(s) < 8:
        return False, "length is less than 8 characters"
    else:
        return True, "no problems"

def validate_comp_8(s):
    if not validate_basic_8(s)[0]:
        return validate_basic_8(s)
    else:
        hasSpecialChar = False
        hasCapital = False
        hasNum = False
        hasLower = False

        for char in s:
            if 97 <= ord(char) <= 122:
                hasLower = True
            if 33 <= ord(char) <= 47 or 58 <= ord(char) <= 64:
                hasSpecialChar = True
            if 48 <= ord(char) <= 57:
                hasNum = True
            if 65 <= ord(char) <= 90:
                hasCapital = True

        if not hasLower:
            return False, "is missing a lowercase letter" 
        elif not hasCapital:
            return False, "is missing a capital letter"
        elif not hasNum:
            return False, "is missing a digit"
        elif not hasSpecialChar:
            return False, "is missing a special character"
        else:
            return True, "no problems"
        
def validate_basic_16(s):
    if len(s) < 16:
        return False, "length is less than 16 characters"
    else:
        return True, "no problems"

def write_output(line, file):
    with open(file, 'a') as f:
        f.writelines(line)

def get_bcrypt_line(p):
    phash = bcrypt.hashpw(p, bcrypt.gensalt())
    line = p + ", " + phash + "\n"
    return line

def get_pbk_line(p):
    phash = pbkdf2_sha256.hash(p)
    line = p + ", " + phash + "\n"
    return line

def get_passwords(f):
    output = set()
    try:
        with open(f) as file:
            for line in file:
                pw = line.split(", ")[0]
                output.add(pw)
    except:
        pass
    return output

if __name__ == "__main__":
    main()
