# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

from itertools import groupby, count


def solution(args):
    def rangify(iterable):
        groups = list(iterable)
        if len(groups) > 2:
            return f"{groups[0]}-{groups[-1]}"
        if len(groups) > 1:
            return f"{groups[0]},{groups[-1]}"
        else:
            return f"{groups[0]}"
    return ','.join(rangify(g) for _, g in groupby(args, key=lambda n, c=count(): n-next(c)))


print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
