# function to create a letter "O"
def create_o():
    print("#" * 9)
    for i in range(3):
        print("#", " " * 5, "#")
    print("#" * 9)


# function to create a letter "H"
def create_h():
    for i in range(5):
        if i == 2:
            print("#" * 9)
        else:
            print("#", " " * 5, "#")

create_o()
print()
create_h()
