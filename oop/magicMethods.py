"""
Dunder __...___ Magic methods are required to compare objects of same class with each other
gt >
lt <
eq = 
str = returns string 
add = + to add objects 
contains = checks keyword we are searching for 
            is keyword in self.title or keyword in self.author
getitem = checks if key received is equal to title author or pages 
"""

class Book:
    def __init__(self, name, author ,pages):
        self.name = name
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"Book: {self.name} Author: {self.author}" 
    
    def __eq__(self, other):
        if self.pages == other.pages:
            return True
    
    def __gt__(self, other):
        if self.pages > other.pages:
            return True
    
    def __lt__(self, other):
        if self.pages > other.pages:
            return True
    
    def __add__(self, other):
       return f"Total pages of both books: {self.pages} + {other.pages} = {self.pages + other.pages}" 
    
    def __contains__(self, keyword):
        if keyword in self.name or keyword in self.author:
            return f"{keyword} found."
            
    def __getitem__(self, key ):
        if key == 'name':
            return f"Key '{key}' is {self.name}."
        elif key == 'author':
            return f"Key '{key}' is {self.author}."
        elif key == 'pages':
            return f"Key '{key}' are in {self.name}: {self.pages}."
        else:
            return f"'{key}' is not available in object."
    
book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry potter and The Philosopher's Stone", "J.k Rowling", 217)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 313)

print(book1) # <- calls str magic method
print(book1 == book2) #if pages are equal then only it will call it and return true otherwise false
print(book2 > book3) #if pages greater return true
print(book2 < book3) #if pages less return true
print(book2 + book3) #returns count of total no of pages of these obj books
print('Rowling' in book2) #returns true if keyword found in book2 
print(book2['pages']) #returns key of what is demanded. so book2 name is revealed. 