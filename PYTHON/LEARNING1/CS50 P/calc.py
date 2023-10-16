#calculator

x = int(input("x: "))
z = input("operation? : ")
y = int(input("y: "))



if z == "-":
    print(x - z)
elif z == "+":
    print(x + z)
elif z == "/":
    print(x / y)
elif z== "//":
    print(x // y)
elif z == "%":
    print(x % y)
else:
    print("please input a valid arithmetic function")
