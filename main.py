from stats import count_words

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")

main()