# Create 12+ Book objects and store in list(library)
# Create program entry point with menu and ask user for menu selection, validate selection
# Define search():
    # Can search by author or title keywords
        # Print:
            # Selected book info
            # Invalid choice
# Define checkout():
    # Check book status
    # If checked out
        # Print message
    # If available:
        # Set status to checked out
        # Set due date for 2 weeks out
        # Call book.degrade()
# Define return(book):  Brendan
    # Return_stack =[ ]
    # Print a list of checked out books
    # Ask user to select their book
    # Add book to return_stack
    # Loop: Check condition of books in returns_stack
        # If condition is below threshold
        # Pop from returns_stack
        # Remove book object from original list
        # If condition above threshold:
        # Update due date to null
        # Update book status to On Shelf


# ==================================================================================================================== #

from Book import *

# ==================================================================================================================== #
# Book Instantiation
# ==================================================================================================================== #

b1 = Book("Of Mice and Men", "John Steinbeck", "On Shelf", 10, None)
b2 = Book("Macbeth", "William Shakespeare", "On Shelf", 8, None)
b3 = Book("Jane Eyre", "Charlotte Brontë", "On Shelf", 2, None)
b4 = Book("Pride and Prejudice", "Jane Austen", "On Shelf", 7, None)
b5 = Book("The Book Thief", "Markus Zusak", "On Shelf", 9, None)
b6 = Book("Animal Farm", "George Orwell", "Checked Out", 10, "02-10-2024")
b7 = Book("Fahrenheit 451", "Ray Bradbury", "On Shelf", 10, None)
b8 = Book("The Catcher in the Rye", "JD Salinger", "On Shelf", 5, None)
b9 = Book("A Game of Thrones", "George R.R. Martin", "On Shelf", 6, None)
b10 = Book("The Odyssey", "Homer", "On Shelf", 6, None)
b11 = Book("A Tale of Two Cities", "Charles Dickens", "On Shelf", 8, None)
b12 = Book("Great Expectations", "Charles Dickens", "On Shelf", 10, None)


# ==================================================================================================================== #
# Program Functions
# ==================================================================================================================== #

def search(book_list):
    print("\nBooks List:")
    for books in book_list:
        print(books)
        print()
    user_input_valid = False
    while not user_input_valid:
        book_selection = []
        user_input = input("Please enter search term: > ")
        print()
        for books in book_list:
            if user_input.capitalize() in books.title or user_input.capitalize() in books.author:
                print(books)
                print()
                book_selection.append(books)
                user_input_valid = True
            else:
                continue
    return book_selection



def checkout(book):
    book_status = book.status
    if book_status == "Checked Out":
        print("This book is already checked out!")
    else:
        book.status = "Checked Out"
        book.set_due_date()
        book.degrade()
        print(f"{book.title} has been checked out! Your due date is: {book.due_date}\n")


def return_book():
    print("Check Out Books List:\n")
    for books in book_list:
        if books.status == "Checked Out":
            print(books)
            print()
        else:
            continue
    user_input_valid = False
    while not user_input_valid:
        user_input = input("Please select your book by title or author: > ")
        for books in book_list:
            if user_input.capitalize() in books.title or user_input.capitalize() in books.author:
                print(books)
                print()
                book_selection2 = books
                user_input_valid = True
            else:
                continue
    return_list.append(book_selection2)
    for book in return_list:
        if book.condition <= 1:
            book.status = "Recycled"
            return_list.remove(book)
            book_list.remove(book)
            print("Your book has been recycled!\n")
        else:
            return_list.remove(book)
            book.status = "On Shelf"
            book.due_date = None
            print("Your book has been returned!\n")


def add_book():
    title = input("What is the book title? > ")
    author = input("What is the book's author? > ")
    new_book = Book(title, author, "On Shelf", 10, None)
    book_list.append(new_book)
    print("\nBook has been added!")

# ==================================================================================================================== #
# Main Program Start
# ==================================================================================================================== #


book_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12]
return_list = []

print("Welcome to the GC Library Terminal")
input_user = " "
user_continue = True

while user_continue:
    input_user = input("What would you like to do today? (Search & Checkout, Return, Add, Exit) ")
    if "search" in input_user.lower():
        book_selection1 = search(book_list)
        if len(book_selection1) > 1:
            print("Multiple books have been found! Please select your book by title:")
            book_selection3 = search(book_selection1)
            book_selection_tf = True
        else:
            book_selection_tf = False
        checkout_flag = False
        while not checkout_flag:
            checkout_yn = input("Would you like to try to checkout this book? (y/n) > ")
            if checkout_yn == 'y':
                if not book_selection_tf:
                    checkout(book_selection1[0])
                    checkout_flag = True
                else:
                    checkout(book_selection3[0])
                    checkout_flag = True
            elif checkout_yn == 'n':
                checkout_flag = True
            else:
                print("Invalid Input")
    elif input_user.lower() == "return":
        return_book()
    elif input_user.lower() == "add":
        add_book()
    elif input_user.lower() == "exit":
        user_continue = False
    else:
        print("Invalid Input, please try again")

