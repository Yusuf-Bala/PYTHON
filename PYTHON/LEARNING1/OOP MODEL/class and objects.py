class newclass:

    def newfunc(self):
        return "python is fun"
    
# new object 
newobj = newclass() 

print(newobj.newfunc())


#
class domath :

    def addition(self, x, y):
        return (x + y)
    
    def subtraction(self, x, y):
        return x - y
    
    def multiplication(self, x, y):
        return x *y 
    
#object
first_object = domath()

print(first_object.addition(3,5))
print(first_object.subtraction(7, 5))
print(first_object.multiplication(7,2))

second_object = domath()

print(second_object.addition(4,8))
print(second_object.subtraction(4,9))
print(second_object.multiplication(6,8))
    
    