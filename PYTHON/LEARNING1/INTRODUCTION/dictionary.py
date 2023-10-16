# #dictionary
words ={"messi":10, "ronaldo":7}
words2 = dict({"messi":10, "ronaldo":"trashplayer"})

print(str(words) + "\n" + str(words2) )

# #

fruit_price = {"apple" : 20, "mango": 40}
print(fruit_price["apple"])
#or
print(fruit_price.get("apple"))


#changing value value to dictionary 

player_number = {"ronaldo" : 7, "messi": 10, "salah" : 4 , "apple" : [1,3,3,4,4] }
player_number["ronaldo"] = 8
print(player_number["ronaldo"])
print(player_number["apple"][2])
#deleting items

del player_number ["messi"]

print(player_number["messi"])


#addding item

player_number["pogba"] = 8

print(player_number)