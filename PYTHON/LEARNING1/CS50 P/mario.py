#this code will print # in many ways 

# for i in range(3):
    # print("x" * 3)
                    #this code will print # in three lines and three rows

# for i in range(3):
    # for j in range(3):
        #print("?")
                        #this code will multiply the ranges and return the print function 
                        # 
# print("x" * 2) #this will print it on thesame line

def get_height():
    height = int(input("height : "))
    while True:
        if height > 0:
            break
    return height

        
def get_lenght():
    lenght = int(input("lenght : "))
    while True:
        if lenght > 2:
            break
        else:
            print("number must be greater than 2")
    return lenght


def main():
    for i in range(get_height()):
        print("#" * get_lenght())
        break

main()