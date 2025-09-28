from collections import defaultdict

def count_words(text):
    words_split = text.split()
    return len(words_split)

def count_characters(text):
    character_dictionary = defaultdict(int)
    for character in text:
        character_dictionary[character] += 1
    return character_dictionary

def sort_on_num(dict):
    return dict["num"]

def create_sorted_list_of_dicts(dictionary_with_all_characters):
    list_of_dicts = []
    for key in dictionary_with_all_characters:
        character_dict_entry = {"char": "a", "num": 0}
        character_dict_entry["char"] = key
        character_dict_entry["num"] = dictionary_with_all_characters[key]
        list_of_dicts.append(character_dict_entry)

    list_of_dicts.sort(reverse=True, key=sort_on_num)

    return list_of_dicts