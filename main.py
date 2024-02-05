from Book import *

# ==================================================================================================================== #
# Book Instantiation
# ==================================================================================================================== #

b1 = Book("Of Mice and Men", "John Steinbeck", "On Shelf", 10, None)
b2 = Book("Macbeth", "William Shakespeare", "On Shelf", 8, None)



# ==================================================================================================================== #
# Program Functions
# ==================================================================================================================== #

def search():
    for books in book_list:
        print(books)
    print()
    user_input_valid = False
    while not user_input_valid:
        user_input = input("Please enter search term: > ")
        for books in book_list:
            if user_input in books.title or user_input in books.author:
                print(books)
                book_selection = books
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


def return_book():
    print("Check Out Books List:")
    for books in book_list:
        if books.status == "Checked Out":
            print(books)
        else:
            continue
    user_input_valid = False
    while not user_input_valid:
        user_input = input("Please select your book by title or author: > ")
        for books in book_list:
            if user_input in books.title or user_input in books.author:
                print(books)
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
        else:
            book.status = "On Shelf"
            book.due_date = None


# ==================================================================================================================== #
# Main Program Start
# ==================================================================================================================== #
book_list = [b1, b2]
return_list = []

print("Welcome to the GC Library Terminal")
input_user = " "
user_continue = True

while user_continue:
    input_user = input("What would you like to do today? (Search & Checkout, Return) ")
    if "search" in input_user.lower():
        book_selection1 = search()
        checkout_flag = False
        while not checkout_flag:
            checkout_yn = input("Would you like to try to checkout this book? (y/n) > ")
            if checkout_yn == 'y':
                checkout(book_selection1)
                print(f"{book_selection1.title} has been checked out! Your due date is: {book_selection1.due_date}")
                checkout_flag = True
            elif checkout_yn == 'n':
                checkout_flag = True
            else:
                print("Invalid Input")
    elif input_user.lower() == "return":
        return_book()
    else:
        print("Invalid Input, please try again")

print(book_list)
print()
print(return_list)

