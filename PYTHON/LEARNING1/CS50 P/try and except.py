def get_height():
    while True:
        try:
            n = int(input("height : "))
            if n > 0:
                return n
        except ValueError:
            print("enter a valid integer")

# get_height()
    # OR

def get_lenght():
    while True:
        try:
            lenght = int(input("lenght : "))
        except ValueError:
            print("enter a valid integer")
        else:
            if lenght>0:
                return lenght
        
get_lenght()
        