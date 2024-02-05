
book_list=[]
return_list=[]
print("Welcome to the GC Library Terminal")
input_user=" "
user_continue=True

while user_continue:
    input_user = input("What would you like to do today? (Search, Return, Checkout) ")
    if input_user.lower() == "search":
        print(book_list)
        pass
    elif input_user.lower() == "return":
        pass
    elif input_user.lower() == "checkout":
        pass
    else:
        print("Invalid Input, please try again")



