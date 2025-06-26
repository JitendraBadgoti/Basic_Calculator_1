# taking the numbers from user

a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))

# asking for the desired operation

print("Enter 1 for addition")
print("Enter 2 for sub")
print("Enter 3 for mul")
print("Enter 4 for div")
print("Enter 5 for fdiv")
print("Enter 6 for remainder")

def tocalculate(x,y):
    while True:
        entered_number = int(input("choose a number from 1 to 6 : "))
        if entered_number == 1 :
            print("The sum of the numbers is :", x + y)
    
        elif entered_number == 2 :
            print("The subtraction of the numbers is :", x - y)
    
        elif entered_number == 3 :
            print("The multiplication of the numbers is :", x * y)
    
        elif entered_number == 4 :
            print("The division of the numbers is :", x / y)
    
        elif entered_number == 5 :
            print("The floor div of the numbers is :", x // y)
    
        elif entered_number == 6 :
            print("The remainder of the numbers is :", x % y)
    
        else :
            print("invalid input")
tocalculate(a,b)
