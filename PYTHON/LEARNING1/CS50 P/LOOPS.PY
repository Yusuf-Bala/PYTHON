#WHILE LOOPS

x = 7
while x < 100:
    # print(x)
    x += 1


# for loops

for i in range(10):
    print("lol")


# while....else 

while True:
    name = input("what is your name : ")
    password = input("what is your password? : ")
    if name.isalpha:
        if password.isalnum:            #is alnum
            print ("login successful")
            print(f"welcome to your account MR {name}")
            break
        else:
            print("let the pasword be alpha numeric!!!!")
    else:
        print("REWRITE NAME IN ALPHABETS")


    