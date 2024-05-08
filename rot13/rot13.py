# https://www.codewars.com/kata/530e15517bc88ac656000716
# One liner, great fun for the whole family

import string


def rot13(message):
    return "".join([string.ascii_letters[int((string.ascii_letters.index(letter) + 13) % 26)+26] if letter.isupper() else string.ascii_letters[int((string.ascii_letters.index(letter) + 13) % 26)] if letter in string.ascii_letters else letter for letter in message])

    letters = string.ascii_letters

    answer = ""

    for letter in message:
        if letter in letters:
            letterIndex = int((letters.index(letter) + 13) % 26)
            answer += (letters[letterIndex+26] if letter.isupper() else letters[letterIndex])
        else:
            answer += letter
    return answer


print(rot13("Test"))  # Grfg
print(rot13("test"))  # grfg
print(rot13("test!!"))  # grfg!!
print(rot13("aAaA!!"))  # grfg!!
