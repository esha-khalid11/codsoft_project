#Simple calculator using function 
#Function for basic arthmetic operations
#Addition of two numbers
def add(a ,b):
    return a+b

#Subtraction of two numbers
def subtract(a ,b):
    return a-b

#Multiplication of two numbers
def multiply( a, b):
    return a*b

#Divsion of two numbers
def division(a ,b):
        if fval or sval!=0:
            return a/b
        else:
            return "Error"
#Modulus of two values        
def modulus(a, b):
    return a%b        
         
#Exponent of two numbers
def exponent(a,b):
    return a**b

#Select any one operation to perform
print("Select the operation:")
print("1:Add(+)")
print("2:Subtract(-)")
print("3:Multiply(*)")
print("4:Divide(/)")
print("5:Modulus(%)")
print("6:Exponential(**)")
#Enter "E" to exit 
print("7:Exit")

#Using While loop and conditional statements to perform the calculation
while(True):
    operator = (input("Enter the operation to perform:"))
    if operator in ('+','-','*','/','%','**','E'):
        if operator=='+':
            fval = int(input("Enter first number:"))
            sval = int(input("Enter second number:"))
            print(add(fval,sval))

        elif operator=='-':
            fval = int(input("Enter first number:"))
            sval = int(input("Enter second number:"))
            print(subtract(fval,sval))

        elif operator=='*':
            fval = int(input("Enter first number:"))
            sval = int(input("Enter second number:"))
            print(multiply(fval,sval))

        elif operator=='/':
            fval = int(input("Enter first number:"))
            sval = int(input("Enter second number:"))
            print(division(fval,sval))

        elif operator=='%':
            fval = int(input("Enter first number:"))
            sval = int(input("Enter second number:"))
            print(modulus(fval,sval))    

        elif operator=='**':
            ffval = int(input("Enter first number:"))
            sval = int(input("Enter second number:"))
            print(exponent(fval,sval))
    
        elif operator=='E':
            print("Process Finished\n Thanks")
            exit()
    else:
        print("This calculator have no such features to execute this program:")
        print("Try Again")       
    

    
    

