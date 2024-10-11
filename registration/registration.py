#This program is designed to create a registration system template for schools
#first step is to create a class for students with different attributes 
newStudents=[]
class Student:
    def __init__(self, firstName, secondName, age, grade):
        self.firstName = firstName
        self.secondName = secondName
        self.age = age
        self.grade = grade
        self.payment = False

    def __repr__(self):
        print(self.firstName,self.secondName,"is a",self.age,"year old grade",self.grade,"student" )

class Registral:

    def registerStudent(firstName,secondName,age,grade):
        global newStudents
        newStudent=Student(firstName,secondName,age,grade)
        newStudents.append(newStudent)
        
    
    def displayStudents():
        if not newStudents:
            print("There are no registered students yet.")
        else:
            for item in newStudents:
                item.__repr__()

    def removeStudents( firstname, lastname):
        for item in newStudents:
            if firstname == item.firstName and lastname == item.secondName:
                newStudents.remove(item)
                print("You have succesfully canceled the registration of the student", firstname,lastname)
            else:
                print("There is no registered student by this name.")
                
    def cont():
          choice = input("do you want to go to the menu? yes/no")
          if choice == "yes":
                Registral.intro()
          elif choice == "no":
                exit()
    def intro():
        print("1.Register a Student")
        print("2.Cancel Registration")
        print("3.View registered students list")
        choice= int(input("Enter your choice "))
        if choice == 1:
            print("Enter your information ")
            firstname= input("Please enter your first name ")
            secondname= input("Please enter your second name ")
            age= input("please enter your age ")
            grade= input("please enter your grade ")
            Registral.registerStudent(firstname,secondname,age,grade)
            print()
            print("You have succesfully registered")  
            Registral.cont()
  
        elif choice == 2 :
            print("Enter the first name and lastname of the student ")
            firstname= input("Please enter your first name ")
            secondname= input("Please enter your second name ")
            Registral.removeStudents(firstname,secondname)
            Registral.cont()
            
        elif choice == 3 :
            Registral.displayStudents()
            Registral.cont()

print("Welcome to Python School registration page")
Registral.intro()


