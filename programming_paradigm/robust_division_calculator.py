def safe_divide(numerator, denominator):
    try :
            result =  numerator/denominator
            print(f"division of the numbers: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print(f"Sorry, division by zero is not allowed.")         

