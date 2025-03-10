import string

def letters_range(input_str):
    start, end = input_str.split('-')
    letters = string.ascii_letters
    return letters[letters.index(start):letters.index(end) + 1]


print(letters_range("a-A"))
