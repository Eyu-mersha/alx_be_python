def perform_operation(num1,num2,operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1*num2
    elif operation == "divide":
        if num2 == 0 :
            return print("the divisor cannot be zero ")
        else:
            return num1/num2
    else:
        print("Error: Please enter a valid operation")
    
