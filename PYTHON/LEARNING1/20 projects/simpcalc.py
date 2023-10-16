def addition(a,b):
    answer = a + b
    print(str(a) , "+" , str(b) , " = " ,  str(answer) , "\n")

def subtraction(a,b):
    answer = a - b
    print(str(a) , "-" , str(b) , " = " , str(answer) , "\n")

def multiplication(a,b):
    answer = a * b
    print(str(a) , "*" , str(b) , " = " , str(answer) , "\n")

def division(a,b):
    answer = a / b
    print(str(a) , "/" + str(b) ,"=" , str(answer) , "\n")

while True:
    print("A. ADDITION       ")
    print("B. SUBTRACTION    ")
    print("C. MULTIPLICATION ")
    print("D. DIVISION       ")
    print("E. EXIT           ")

    choice = input("input your choice : ")
    choice = choice.lower()


    if choice == "a":
        try:
            print("addition")
            choice_a = int(input("first number : "))
            choice_b = int(input("second number : "))
        except ValueError:
            print("value must be an integer")
        else:
            addition(choice_a, choice_b)

    elif choice == "b":
        try:
            print("subtraction")
            choice_a = int(input("first number : "))
            choice_b = int(input("second number : "))
        except ValueError:
            print("value must be an integer")
        else:
            subtraction(choice_a, choice_b)

    elif choice == "c":
        try:
            print("multiplication")
            choice_a = int(input("first number : "))
            choice_b = int(input("second number : "))
        except ValueError:
            print("value must be an integer")
        else:
            multiplication(choice_a, choice_b)

    elif choice == "d":
        try:
            print("division")
            choice_a = int(input("first number : "))
            choice_b = int(input("second number : "))
        except ValueError:
            print("value must be an integer")
        else:
            division(choice_a, choice_b)

    elif choice == "e":
        print("end of program")
        quit()
    
    
    

