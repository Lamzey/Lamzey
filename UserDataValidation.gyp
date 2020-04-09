import random
import string
import re
import pickle

print("Please Enter Your First Name: ")
firstName = input()

print("")
print("Please Enter Your Last Name: ")
lastName = input()

print("")
print("Please Enter Your E-mail: ")
email = input()

user = firstName[0:2]+lastName[-2:]

def randomString(stringLength=5):
    """ Generate a random string of a fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) 
    for i in range(stringLength))
print("")
print("Are you satisfied with this password?, Please input Yes or No, Note your letters should start with capitals ")
ans = input()
if ans == 'Yes':
    User = {
        "firstName: " + firstName,
        "lastName: " + lastName,
        "email: " + email,
        "password: " + user + randomString(),
    }
    f = open("file.pkl","wb")
    pickle.dump(User,f)
    f.close
    print("")
    print(User)

    exit()
else:
    print("")
    print("Please enter the password of your choice, must be 7 digits in length. " + "Password must Start with capital letter and must entail numbers and this characters => [@,#,$]")
    p = input("")
    x = True
    while x:
        if(len(p) < 7):
            print("")
            print("Please enter your password again, make sure it's not less than seven digits")
            p = input("")
        elif not re.search("[a-z]",p):
            break
        elif not re.search("[0-9]",p):
            break
        elif not re.search("[A-Z]",p):
            break
        elif not re.search("[$#@]",p):
            break
        elif re.search("\s",p):
            break
        else:   
            User = {
            "firstName: " + firstName,
            "lastName: " + lastName,
            "email: " + email,
            "password: " + p,
            }
            
            f = open("file.pkl","wb")
            pickle.dump(User,f)
            f.close
            print("")
            print(User)
            x = False
            break
if x:
    print("")
    print("Not a Valid Password")