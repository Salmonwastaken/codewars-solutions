# https://www.codewars.com/kata/55b42574ff091733d900002f

def friend(x):
    return [friend for friend in x if len(friend) == 4]
