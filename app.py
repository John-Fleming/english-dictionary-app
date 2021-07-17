import json

definitions = json.load(open("data.json"))

def look_up_defintion(word):
  formatted_word = word.lower().replace(' ', '')

  if formatted_word in definitions:
    return definitions[formatted_word]
  else:
    return 'Could not find that word'
  
word_to_search = input('Enter a word to look up: ')

print(look_up_defintion(word_to_search))
