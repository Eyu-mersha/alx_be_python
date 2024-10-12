import hashlib
import getpass
users=[]
class Credentials:
    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password 
    def __repr__(self):
        return print(f"name:{self.name} Username: {self.username} Password: {self.password}")
    def createUser(name,username,password):
        credential = Credentials(name,username,Operations.hash_password(password))
        users.append(credential)
        print("\n-------- Sign up successful.---------")
    def checkUser(username,password):
        for i in users:
            if username == i.username and Operations.hash_password(password)== i.password:
                print(f"\n\n Welcome to your Dashboard dear {i.name} \n\n")
                
            else: 
                print("------Wrong username or password")

class Operations:                 
    def hash_password(password):
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        return sha256.hexdigest()
    def login():
        print("\n\n\n------------------------- Login -----------------------------\n\n")
        print("Submit the required information please")
        username = input("Enter your phone number:  ")
        password = getpass.getpass("Enter your password: ")
        Credentials.checkUser(username,password)
    def signUp():
        print("\n\n\n-------------------------Sign up form  -----------------------------\n\n")
        print("Submit the required information please")
        name = input("Enter your name:  ")
        username = input("Enter your phone number:  ")
        password = getpass.getpass("Enter your password: ")
        Credentials.createUser(name,username,password)


print("\n\n\n-------------------------Welcome to Gulit Online Store-----------------------------\n\n")
print("       1. Sign up ")
print("       2. Login to your dashboard  \n\n")
choice = int(input(" Enter your choice: "))

if choice == 1:
    Operations.signUp()
    Operations.login()
elif choice == 2:
    Operations.login()
else: 
    print("You have entered a wrong number.")

    
