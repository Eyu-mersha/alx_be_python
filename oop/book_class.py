class Book:
    def __init__(self,author,title,year):
        self.author = author
        self.title = title
        self.year = year

    def __del__(self):
        print ("Deleting {self.title}")
    
    def __str__(self):
        print("{self.title} by {self.author}, published in {self.year}")