
def divideNumbers ():
    try :
            Num1 = float(input("Enter the first number"))
            Num2 = float(input("Enter the second number"))
            result =  Num1/Num2
            print(f"division of the numbers: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print(f"Sorry, division by zero is not allowed.")         

divideNumbers()




