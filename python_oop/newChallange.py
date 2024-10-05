import random

fullName = input("What is yor name ? ")
print("Welcome to the site", fullName)

print("Please select the action you want to perform")
print("1. Create an account")
print("3. Deactivate account")

choice =int(input("Input your selection ")) 

class Account:

    def __init__(self, name , birthyear,id, issueDate, expireDate, accountBalance=0):
        self.name = name # Instance attribute
        self.age = 2024 - birthyear # Instance attribute
        self.issueDate = issueDate
        self.expireDate = expireDate
        self.id= id
        self.accountNo= random.randint(1000000, 9999999)
        self.accountBalance=0
    def deposit(self,amount):
        self.accountBalance = self.accountBalance + amount
        return self.accountBalance
    def withdrawal(self,amount):
        self.accountBalance = self.accountBalance - amount
        return self.accountBalance


if choice == 1:
    print(" Lets gather your personal information")
    birthdate= int(input("Please enter your birthday with a format YMD "))
    identificationNo = input("Please enter your birthday with a format YMD ")
    issueDate =int(input("Please enter the issue date of your ID card "))
    expireDate =int(input("Please enter the expiration date of your ID card "))
    account = Account(fullName, birthdate, identificationNo, issueDate, expireDate)
    print("You have succesfully created an account at our bank.")
    print("Account number: ",account.accountNo)
    print("1. Show Balance")
    print("2. Manage your account")
    choice =int(input("Input your selection "))
    if choice == 1:
        print("Account number ",account.accountNo," a balance of ",account.accountBalance, " birr")
    elif choice == 2:
        print("1. Make a deposit")
        print("2. Make a withdrawal")
        choice =int(input("Input your selection "))
        if choice == 1:
            amount= int(input("please enteer the deposit amount: "))
            account.deposit(amount)
            print("You have successfully deposited ",amount," birr to account no ",account.accountNo,". Your current Balance is ",account.accountBalance)
else:
    print("abebe")
