# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(lst):
    non_zero = [n for n in lst if n != 0]
    return non_zero + ([0] * (len(lst) - len(non_zero)))
