#adding 20 to 50

a = lambda x : x + 50
print(a(20))

#lambda args 
#2 args 

store_lambda = lambda x, y : x * y
print(store_lambda(20,40))

store_lambda3 = lambda x , y , z : x * y // z
print(store_lambda3(10,20,30))

#lambda and functions 

def new_args(k):
    return lambda x : x * k

new_double = new_args(10) # value of k
new_triple = new_args(20)
print(new_double(10),"\n", new_triple(20)) # value of x