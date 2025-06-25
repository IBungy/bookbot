def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(string):
    big_string = string.split()
    num_words = len(big_string)
    return num_words
    

words_in_book = word_count("books/frankenstein.txt")  
print(f"{words_in_book} words found in the document")

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

if __name__ == "__main__":
    main()