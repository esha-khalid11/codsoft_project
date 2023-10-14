import random
import string

print('RANDOM PASSWORD GENERATOR')
print('Your random password includes')
print(' 1:Letter\n','2:UpperCase\n','3:LowerCase\n','4:Hexdigits\n','5:Punctuation')
max_length = int(input("Enter the maximum length you want:"))

#function for generating random password according to desired length
def generated_password(passlength):

    set1 = string.ascii_letters
    set2 = string.ascii_uppercase
    set3 = string.ascii_lowercase
    set4 = string.digits
    set5 = string.punctuation

    password = f"{set1}{set2}{set3}{set4}{set5}"
    passlist =list(password)
    random.shuffle(passlist)
    randompass = "".join((passlist[:passlength]))
    return randompass
 
#for loop for printing random password and enter 0 to exit the loop
for _ in range(1, max_length):
    passlength = int(input("Enter the length of password (or enter 0 to exit): "))
    
    if passlength == 0:
        break  # Exit the loop if 0 is entered
    
    if 1 <= passlength <= max_length:
        print("Your password is:")
        print(generated_password(passlength))
    else:
        print("Invalid password length.")

print("Hope you like it Thanks")





















   



   
    


