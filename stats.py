from collections import defaultdict

def count_words(text):
    words_split = text.split()
    return len(words_split)

def count_characters(text):
    character_dictionary = defaultdict(int)
    for character in text:
        character_dictionary[character] += 1
    return character_dictionary