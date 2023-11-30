def create_file():
    my_file = open('myfile.txt', 'w')
    my_file.write('Hello file world!')
    my_file.close()


def open_file():
    with open('myfile.txt', 'r') as f:
        print(f.read())

create_file()
open_file()






