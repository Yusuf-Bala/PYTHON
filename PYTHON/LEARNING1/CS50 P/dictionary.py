# code dictionary.py     creating the file
words = set()


def check(word):
    if word.lower() in words:  # .lower().... converts the input to lower case 
        return True            #if the argument passed in word is in the words set then return true else return false
    else:
        return False
    
def load(dict):
    file = open(dict, "r") #this will open the file dictionary
    for line in file:           #for each line in the file dictionary
        word = word.rstrip()    #this strips off the whitespaces, \n and \t at the end of the lines
        words.add(word)         #add the lines to words
    close(file)                 #close the file
    return True                     #return


def size():
    return len(words)

def unload():
    return True
