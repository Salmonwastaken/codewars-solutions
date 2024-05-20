# https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic(val):
    power = len(str(val))
    total = 0

    for i in str(val):
        total += pow(int(i), power)

    return val == total


narcissistic(153)
