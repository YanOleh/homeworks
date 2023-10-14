

def oops():
    name = "Oleh"
    print(name[4])

def errors():
    try:
        oops()
    except IndexError:
        print("Oops! index error.  Try again...")

errors()