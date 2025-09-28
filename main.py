from stats import count_words, count_characters

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    book_text = get_book_text("books/frankenstein.txt").lower()
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    print(f"Found {num_words} total words")
    print(num_characters)

main()