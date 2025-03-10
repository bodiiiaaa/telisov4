def correct_sentence(text: str) -> str:
    return text.capitalize().rstrip('.') + '.'

print(correct_sentence("hello world"))
print(correct_sentence("Python Community"))
