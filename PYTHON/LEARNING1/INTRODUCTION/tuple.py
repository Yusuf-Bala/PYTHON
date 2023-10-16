# #tuples 
players = ("mane", 'salah', 'ronaldo','messi') #tuples can either be stored in a bracket
players2 = "messi", "ronaldo", "kane","son " #or without a bracket but with a comma separating the values

print(players)
print(players2)

# creating single tuples

fruits = ("orange") # not tuple
fruits2 = ("orange",) # tupple

print(fruits)
print(fruits2)


tupple methodds
list in tupple

mixed = ("mango", [10,20,30,40])
# print (mixed[1])

#access items
fruits=("mango","banana","apple","lorem","ipsum")
# print(fruits[0:2])

#update tuple

# fruits = ("orange", "apple")
# print(fruits)

#tuple concatenation 
fruits1 = ("orange", "pine")
fruits2 = ("apple", "banana")
allfruits12 = fruits1 + fruits2
allfruits11 = fruits1[1] + fruits2[1]

# print(allfruits)

#delete tuple

delete = ("poo", "party", "high")

del delete 
print(delete)