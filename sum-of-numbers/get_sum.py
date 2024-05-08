# https://www.codewars.com/kata/55f2b110f61eb01779000053

def get_sum(a, b):
    if a == b:
        return a
    return sum(range(min(a, b), max(a, b)+1))


print(get_sum(0, 1))
print(get_sum(0, -1))
