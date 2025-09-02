name="my name is michael"
sir_name="scofield "
print(f"this is my all detail {name} {sir_name}")
word="michael scofield"
print(word[0:7:2]) # this is for string slicing
print(len(word)) # this is to find length of string
print(word.endswith("mar")) # this return true if gives last word of string otherwise false
print(word.capitalize()) # it convert the first word as capital letter 
print(word.title()) # this convert all words after space as capital
print(word.find("p")) # this return the indexing of to find word 
print(word.replace("michael","lincon")) # this is to replace the older word with new word
story = "i am breaking prison \n as i miss my brother \t i want to go home"
# \n for new line anfd \t for tab
print(story)
user  = str(input("enter good words "))
print(user)

print(user.lower()) # it convert all words in small letter
print(user.upper()) # it convert all words in capital letter