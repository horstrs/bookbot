def print_all_in_new_line(list_of_dict):
    for entry in list_of_dict:
        if not entry["char"].isalpha():
            continue
        print(f"{entry["char"]}: {entry["num"]}")

def print_report(words, characters):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    print_all_in_new_line(characters)
    print("============= END ===============")
