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