from stats import count_words, count_characters, create_sorted_list_of_dicts
from report_printing import print_report
import sys


def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path).lower()
    num_words = count_words(book_text)
    character_dict = count_characters(book_text)
    sorted_list_of_dicts = create_sorted_list_of_dicts(character_dict)
    print_report(file_path, num_words, sorted_list_of_dicts)    

main()