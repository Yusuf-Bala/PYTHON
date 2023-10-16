x = open("new.txt" , "w")

x.write("this is newtext")
x.close()

f = open ("new.txt", "r")

file_name = f.read()
f.close()

print(file_name)