class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}."
class EBook(Book):
    def __init__(self,title,author,file_size):
        self.file_size = file_size
        super().__init__(title, author)
class PrintBook(Book):
    def __init__(self, title, author,page_count):
        super().__init__(title, author)
        self.page_count = page_count
    