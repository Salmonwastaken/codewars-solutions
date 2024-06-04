# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/

import itertools


def permutations(string: str) -> list[str]:
    return list(set([''.join(p) for p in itertools.permutations(string)]))
