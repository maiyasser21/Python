class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(f'The title of the book is: {self.title} and the author is: {self.author}')
        

book=Book("eat pray love","somedude")
book.display()
        