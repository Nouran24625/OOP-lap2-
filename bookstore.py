class Item:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def update_details(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_details(self):
        return f"{self.title} by {self.author} - Price: ${self.price}"

class Book(Item):
    def __init__(self, title, author, price, isbn, genre, num_pages):
        super().__init__(title, author, price)
        self.isbn = isbn
        self.genre = genre
        self.num_pages = num_pages
    
    def get_details(self):
        return f"Book: {super().get_details()} - ISBN: {self.isbn}, Genre: {self.genre}, Pages: {self.num_pages}"
    
class Magazine(Item):
    def __init__(self, title, author, price, issue_number, pub_date, editor):
        super().__init__(title, author, price)
        self.issue_number = issue_number
        self.pub_date = pub_date
        self.editor = editor
    
    def get_details(self):
        return f"Magazine: {super().get_details()} - Issue: {self.issue_number}, Publication Date: {self.pub_date}, Editor: {self.editor}"

class DVD(Item):
    def __init__(self, title, author, price, director, duration, genre):
        super().__init__(title, author, price)
        self.director = director
        self.duration = duration
        self.genre = genre
    
    def get_details(self):
        return f"DVD: {super().get_details()} - Director: {self.director}, Duration: {self.duration}, Genre: {self.genre}"

class Bookstore:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def search_item_by_title(self, title):
        for item in self.inventory:
            if item.title.lower() == title.lower():
                return item
        return None

    def search_item_by_author(self, author):
        for item in self.inventory:
            if item.author.lower() == author.lower():
                return item
        return None

    def search_item_by_genre(self, genre):
        genre_items = [item for item in self.inventory if isinstance(item, Book) and item.genre.lower() == genre.lower()]
        return genre_items

    def calculate_total_sales(self):
        total_sales = sum(item.price for item in self.inventory)
        return total_sales

class Customer:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.cart = []

    def search_item(self, bookstore, title):
        item = bookstore.search_item_by_title(title)
        if item:
            return item.get_details()
        else:
            return "Item not found."

    def add_to_cart(self, item):
        self.cart.append(item)

    def view_cart(self):
        return [item.get_details() for item in self.cart]

    def checkout(self):
        total_cost = sum(item.price for item in self.cart)
        self.cart = []
        return total_cost

# Create a Bookstore instance
bookstore = Bookstore()

# Add items to the inventory
book1 = Book("Python Programming", "John Doe", 25.99, "978-0134444321", "Programming", 400)
magazine1 = Magazine("Tech Today", "Jane Smith", 5.99, 123, "2022-10-01", "Editor X")
dvd1 = DVD("Movie Title", "Director Y", 19.99, "Director Y", "2 hours", "Action")

bookstore.add_item(book1)
bookstore.add_item(magazine1)
bookstore.add_item(dvd1)

# Register a customer
customer1 = Customer("Maria", "maria@gmail.com", 37)

# Perform actions
print(customer1.search_item(bookstore, "Python Programming"))
customer1.add_to_cart(book1)
print(customer1.view_cart())
print("Total Cost:", customer1.checkout())