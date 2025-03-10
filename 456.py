import string

def generate_hashtag(text):
    text = ''.join(c for c in text if c not in string.punctuation).title().replace(" ", "")
    return "#" + text[:140]

print(generate_hashtag("Python Community"))
