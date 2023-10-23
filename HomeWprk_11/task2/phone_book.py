from functions import open_phone_book
from functions import add_new_user
from functions import find_contacts


file_name = 'DataBase.json'


def start_program():
    print("""Hello! Select an action: 
    1. View the entire phone book
    2. Search users in the phone book
    3. Add new user """)
    select_action = int(input('Enter number: '))
    if select_action == 1:
        open_phone_book(file_name)
    elif select_action == 2:
        find_contacts(file_name)
    elif select_action == 3:
        add_new_user()


start_program()
