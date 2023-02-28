# 13. Check if a string is composed of all lower case characters
# ----------------------------------------------------------------
sentence = "Faith is hard to live by, but worth holding on to."
if sentence.islower():
    print("All lowercase letters")
else:
    print("Not all letters are lowercases")


# 16. Reverse the string “hello world”
# ----------------Method 1-----------------
mystring = 'hello world'
length = len(mystring)
index = length-1
while index >= 0:
    print(mystring[index], end='')
    index -= 1
# -------------------Method 2--------------
# convert string to list, invoke reversed method and convert it back to string.
mystring = 'hello world'
mylist = list(mystring)
mylistReversed = mylist.__reversed__()
mystring = ''.join(mylistReversed)
print(mystring)


# 20. Uppercase first and last character of a string
# ------------------------------------------------------
sentence = 'faiTH'
length_of_sentence = len(sentence)
print(sentence[0].upper() + sentence[1:-1] + sentence[-1].lower())


# 28. Check if all characters in a string are alphanumeric
# ---------------------------------------------------------
sentence = "Happin12@ss"
if sentence.isalnum():
    print("All alpha numeric..")
else:
    print("Not all alpha numeric..")


# 34. Capitalize the first character of each word in a string
# ------------------------Method 1------------------------------------
sentence = "Faith is hard to live by, but worth holding on to"
sentenceToList = sentence.split(" ")
lengthOfList = len(sentenceToList)
newList = []
# for, to iterate over the list
for word in sentenceToList:
    lengthOfWord = len(word)
    # for, to iterate over the word in list
    for index in range(lengthOfWord+1):
        if index == 0:
            newWord = word[index].upper()+word[1:]
            newList.append(newWord)
sentence = " ".join(newList)
print(sentence)
# -------------------------Method 2------------------------------
sentence = "Faith is hard to live by, but worth holding on to"
print(sentence.title())
