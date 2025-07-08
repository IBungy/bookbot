from stats import word_count
from stats import character_count
from stats import sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    book_text = get_book_text("books/frankenstein.txt")
    words_found_in_document = word_count(book_text)
    characters_found = character_count(book_text)
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_found_in_document} total words")
    print("--------- Character Count -------")
    for item in sorted_list(characters_found):
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()