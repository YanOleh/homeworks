import json


file_name = 'DataBase.json'

def load_db(file_name, mode='r', data=None):
    if mode == 'r':
        with open(file_name, 'r') as pb:
            return json.load(pb)
    elif mode in ('w', 'a'):
        with open(file_name, 'w' if mode == 'w' else 'a') as pb:
            json.dump(data, pb, ensure_ascii=False, indent=2)

def open_phone_book(file_name):
    users = load_db(file_name)
    found_contacts = []

    for i, user in enumerate(users['subscriber'], 1):
        found_contacts.append(user)
        print(f"{i}. {user}")
    change = int(input('Do you want to make changes: 1.Delete user, 2.Some record, 3.Exit ?: '))
    if change == 1:
        delete_user(change, found_contacts, users)
    elif change == 2:
        change_user_data(change, found_contacts, users)
    else:
        print('Best wishes!')

def change_user_data(change, found_contacts, users):
    if change == 2:
        try:
            choice = int(input('Enter position number to update: '))
            if 1 <= choice <= len(found_contacts):
                chosen_contact = found_contacts[choice - 1]
                chosen_func = int(input('What do you want to change: 1. Number, 2. First name, 3. Last name, 4. City?: '))
                if chosen_func == 1:
                    new_phone = input('Input new phone number: ')
                    chosen_contact['phone_number'] = new_phone
                elif chosen_func == 2:
                    new_first_name = input('Input new first name: ')
                    chosen_contact['first_name'] = new_first_name
                elif chosen_func == 3:
                    new_last_name = input('Input new last name: ')
                    chosen_contact['last_name'] = new_last_name
                elif chosen_func == 4:
                    new_city_name = input('Input new city name: ')
                    chosen_contact['city'] = new_city_name

                load_db('DataBase.json', 'w', users)
                print('Changes saved!')

        except ValueError:
            print('Invalid input')
    else:
        print('Best wishes!')

def delete_user(change, found_contacts, users):
    if change == 1:
        try:
            choice = int(input('Enter position number to delete: '))
            if 1 <= choice <= len(found_contacts):
                chosen_contact = found_contacts[choice - 1]
                users['subscriber'].remove(chosen_contact)
                load_db(file_name, 'w', users)
                print('Changes saved!')
        except ValueError:
            print('Invalid input')

def add_new_user():
    add_first_name = input('Add first name: ')
    add_last_name = input('Add last name: ')
    add_city = input('Add city: ')
    add_phone_number = input('Add phone number(0(000)-000-00-00): ')

    new_user = {
        "first_name": add_first_name,
        "last_name": add_last_name,
        "city": add_city,
        "phone_number": add_phone_number
    }

    data = load_db('DataBase.json', "r")
    data['subscriber'].append(new_user)
    load_db('DataBase.json', 'w', data)
    print('Changes saved!')

def find_contacts(file_name):
    search_data = input('Enter first name / last name / city / phone number: ')

    users = load_db(file_name)
    found_contacts = []
    for user in users['subscriber']:
        if user['first_name'] == search_data:
            found_contacts.append(user)
        elif user['last_name'] == search_data:
            found_contacts.append(user)
        elif user['city'] == search_data:
            found_contacts.append(user)
        elif user['phone_number'] == search_data:
            found_contacts.append(user)
    if not found_contacts:
        print(f"User with name {search_data} not found.")
        return


    print(f"All users with name {search_data}:")
    for i, user in enumerate(found_contacts, 1):
        print(f"{i}. {user}")
    change = int(input('Do you want to make changes: 1.Delete user, 2.Some record, 3.Exit ?: '))
    if change == 1:
        delete_user(change, found_contacts, users)
    elif change == 2:
        change_user_data(change, found_contacts, users)
    else:
        print('Best wishes!')
