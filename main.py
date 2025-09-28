from stats import count_words, count_characters, create_sorted_list_of_dicts

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

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

def main():
    book_text = get_book_text("books/frankenstein.txt").lower()
    num_words = count_words(book_text)
    character_dict = count_characters(book_text)
    sorted_list_of_dicts = create_sorted_list_of_dicts(character_dict)
    print_report(num_words, sorted_list_of_dicts)    

main()