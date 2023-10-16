x = input("x : ")
y = input("y : ")
y = int(y)
x = int(x)

if x > y:
    print(f"{x} is greater than {y}")
elif y > x:
    print(f"{y} is greater than {x}")
else:
    print(f"{x} and {y} are equal")
