#listss
players = ['ronaldo', 'messi',2,'pessi',True]
print(players)
print(players[1])

# list index
print(len(players)) #5
print(players[1:3]) #['messi', 2]
print(players[0]) #ronaldo
print(players[-2]) #pessi


# list methods
fruits = ['lime', 'lemon', 'orange', 'apple']

#changing method

# fruits[2] = "lakh"
# print(fruits)

#appending method

# fruits.append('lakh')
# fruits.append('lakh'[2]) #this will only add the secon letter of the added fruit
# print(fruits)

# delete

# del fruits[2]
# print(fruits)

#insert

#fruits.insert(2,'lakh')
print(fruits[:-2])