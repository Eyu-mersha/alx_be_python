def safe_divide(numerator, denominator):
    try :
            num = float(numerator)
            denom = float(denominator)
            result =  num/denom
            print(f"division of the numbers: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print(f"Sorry, division by zero is not allowed.")         

