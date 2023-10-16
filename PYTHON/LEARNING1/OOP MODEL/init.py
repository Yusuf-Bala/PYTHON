class init:

    def __init__ (self):
        self.a = "lemon"

obj = init()

print(obj.a)

class init2:

    def __init__ (self, name, age):
         self.name = name #input("what is your name")
         self.age = int(age)  #input("how old are you")

obj2 = init2("yusuf",10)  #(input('what is your name', "\n", input('how old are you')))

print(obj2.name)
print(obj2.age)


class players:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("hello  dev " + self.name + str( self.age))

obj3 = players("ade", 7)
obj3.intro()
print(obj3.name)
del obj3.age
obj3.intro() #will return an error 

#modifying object property
obj3.age = 20