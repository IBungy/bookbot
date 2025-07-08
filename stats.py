def word_count(string):
    big_string = string.split()
    num_words = len(big_string)
    return num_words

def character_count(string):
    characters = {}
    lower = string.lower()
    for char in lower:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] = characters[char] + 1
    return characters

def sort_on(item):
    return item["num"]

def sorted_list(characters):
    dictionaries = []
    for char, count in characters.items():
        dictionaries.append(dict(char=char, num=count))
    dictionaries.sort(reverse=True, key=sort_on)
    return dictionaries
