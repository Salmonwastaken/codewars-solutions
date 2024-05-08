# https://www.codewars.com/kata/52fba66badcd10859f00097e
import re


def disemvowel(string_):
    clean = re.sub("(?i)[aeiou]", "", string_)

    return clean


string = "This website is for losers LOL!"
print(disemvowel(string))
