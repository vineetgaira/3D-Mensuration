def user_select_shape():
    valid_choices={1,2,3,4,5,6,7}
    while True:
        try:
            choice=int(input("Enter your choice :"))
            if choice in valid_choices:
                return choice
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a valid integer choice.")
    
def user_select_property():
    valid_choices={1,2}
    while True:
        try:
            choice=int(input("Enter your choice :"))
            if choice in valid_choices:
                return choice
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a valid integer choice.")