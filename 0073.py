def second_index(text: str, target: str):
    first = text.find(target)
    if first == -1:
        return None

    second = text.find(target, first + 1)
    return second if second != -1 else None

print(second_index("sims", "s"))
print(second_index("find the river", "e"))
print(second_index("hi", "h"))
