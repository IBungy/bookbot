from stats import word_count
from stats import character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    words_found_in_document = word_count(book_text)
    characters_found = character_count(book_text)
    print(f"{words_found_in_document} words found in the document")
    for char, count in list(characters_found.items())[:10]:
        print(f"'{char}': {count}")

if __name__ == "__main__":
    main()