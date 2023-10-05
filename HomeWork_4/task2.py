phone_number = input('Enter phone number: ')

if phone_number.isdigit() and len(phone_number) == 10:
    print('Cerect phone number')
else:
    print('Your number must consist only of numbers and be equal to 10 characters')
