from stats import word_count
from stats import character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
    
with open("books/frankenstein.txt", 'r') as f:
    book_text = f.read()
words_found_in_document = word_count(book_text)
print(f"{words_found_in_document} words found in the document")

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

if __name__ == "__main__":
    main()