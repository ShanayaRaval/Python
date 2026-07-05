class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(f"You have borrowed '{self.title}'.")

    def ret_book(self):
        self.is_borrowed = False
        print(f"You have returned'{self.title}'")

b1 = Book("As Good As Dead", "Holly Jackson")
b2 = Book("Harry Potter", "J.K Rowling")
b3 = Book("The Blue Umbrella", "Ruskin Bond")

b2.borrow()
b1.borrow()

b3.ret_book()