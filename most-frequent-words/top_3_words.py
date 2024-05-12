# https://www.codewars.com/kata/51e056fe544cf36c410000fb
# Figuring out the regex on this took me forever, still not perfect.
# line 19 is a workaround, too bad about the performance.
# I refused to use a Counter for some reason.
# I really ought to learn how to properly add tests, rather than just calling and manually checking :)

import re


def top_3_words(text):
    lower = text.lower()
    p = re.compile(r"[a-z']+")

    if not p.search(lower):
        return []

    count_map = {}

    for match in p.finditer(lower):
        word = match.group()
        if re.match(r"^[\'\s]+$", word) is not None:
            continue
        count_map[word] = count_map.get(word, 0) + 1

    return sorted(count_map, key=count_map.get, reverse=True)[:3]


print(top_3_words("a a a  b  c c  d d d d  e e e e e"))  # ["e", "d", "a"]
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))  # ["e", "ddd", "aa"]
print(top_3_words("  //wont won't won't"))  # ["won't", "wont"]
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))  # ['a', 'of', 'on']
print(top_3_words("  ...  "))  # []
print(top_3_words("  '  "))  # []
