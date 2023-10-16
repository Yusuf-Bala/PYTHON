# this program wiill replace a word in a sentence with another word
# this uses the .replace method
#  .replace(initial, last)
def replacement():

    str = "hi guys.. hey hey hey"
    word_to_replace = input("word to replace: ")
    word_replacement = input("word replacement: ")

    print(str)
    print (str.replace(word_to_replace, word_replacement))

replacement()