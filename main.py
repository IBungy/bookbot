from stats import word_count
from stats import character_count
from stats import sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    words_found_in_document = word_count(book_text)
    characters_found = character_count(book_text)
    print(f"Analyzing book found at ...")
    print("----------- Word Count ----------")
    print(f"Found {words_found_in_document} total words")
    print("--------- Character Count -------")
    for item in sorted_list(characters_found):
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()