#functions 
def hello_function():
    print("hello dev")

#function calling
hello_function()

#passing information into a function

def hello_function1(name):
    print("hello_dev " + name)

#calling function 

hello_function1("ronaldo")
hello_function1("messi")

#functions with default value #this function will return the default value if no value is being provided when calling it 

def hello_function2(name = "pogba"):
    print("hello_dev " + name)

hello_function2()
hello_function2("messi")

#paralist

def new_fruit(fruit):
    for x in fruit:
        print(x)

fruit_name = ["fig","apple","banana","peach"]
new_fruit(fruit_name)