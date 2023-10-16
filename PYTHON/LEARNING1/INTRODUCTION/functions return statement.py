def numbers(x):
    return 10 * x
    # print("hello" + x )

# number_list = {10,20,30}
print(numbers(10))

# key value args

# def fruits(fruit1, fruit2, fruit3):
    # print("this is fruit1 " + fruit1)
    # print("this is fruit2 " + fruit2)
    # print("this is fruit3 " + fruit3)

# fruits(fruit1="mango", fruit2="banana", fruit3="apple")


#arbitrary args

def fruits(*fruit):
    print("this is " + fruit [2])

fruits("fig","apple","peach") #tupple