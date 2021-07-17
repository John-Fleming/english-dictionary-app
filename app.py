import json
from difflib import get_close_matches

definitions = json.load(open("data.json"))

def find_closest_word(word):
  matched_word = get_close_matches(word, definitions.keys(), cutoff=0.8)

  if len(matched_word):
    user_feedback = input("Did you mean '%s' instead? Enter y or n: " % matched_word[0])
    return definitions[matched_word[0]] if user_feedback.lower() == 'y' else None

def look_up_defintion(word):
  formatted_word = word.lower().replace(' ', '')
  
  if formatted_word in definitions:
    return definitions[formatted_word]
  else:
    matched_word = find_closest_word(formatted_word)
    return matched_word if matched_word is not None else 'Could not find that word in dictionary'
  
word_to_search = input('Enter a word to look up: ')

result = look_up_defintion(word_to_search)

if type(result) == list:
  for definition in result:
    print(definition)
else:
  print(result)
