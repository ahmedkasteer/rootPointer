"""
Aggregation is basically where one obj Library contains references to one or more 
INDEPENDENT objects (the parts) Books 
"""
#two independent classes 

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    
    def addBook(self, book):
        self.books.append(book)
    
    
    def listBooks(self):
        return [f"{book.title} by {book.author}"for book in self.books]



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book1 = Book('Harry Potter', 'JK Rowling')
book2 = Book('The Hobbit', 'JRR Tolkein')
book3 = Book('The Color of Magic', 'Terry Pratchet')

library = Library('***************New York Public Library***************')

library.addBook(book1)
library.addBook(book2)
library.addBook(book3)


print(library.name)

for book in library.listBooks():
    print(book)
