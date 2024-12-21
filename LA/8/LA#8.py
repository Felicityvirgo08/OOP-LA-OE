print("LA#8")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

Book1 = Book("A Gentle Reminder", "Bianca Sparacino")
print("First Book Title and Author:", Book1.title, Book1.author)

Book1.author = "Bianca Sparacino"

Book2 = Book("Florante At Laura", "Francisco Balagtas")
print("Second Book Title and Author:", Book2.title, Book2.author)