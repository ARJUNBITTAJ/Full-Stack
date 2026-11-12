'''TASK3: Show method overriding using str () or any custom method in Python.'''

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"


b1 = Book("Atomic Habits", "James Clear", 320)

print(b1)