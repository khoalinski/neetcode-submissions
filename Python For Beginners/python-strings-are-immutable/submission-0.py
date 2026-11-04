def remove_fourth_character(word: str) -> str:
    first_3 = word[0:3]
    last = word[4:]

    return first_3 + last


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
