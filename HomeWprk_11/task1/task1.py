def create_file():
    with open('my_file.txt', 'w') as f:
        f.write('Hello file world')


def open_file():
    with open('my_file.txt', 'r') as f:
        print(f.read())


create_file()

open_file()

