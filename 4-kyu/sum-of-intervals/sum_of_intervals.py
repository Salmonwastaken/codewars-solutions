# https://www.codewars.com/kata/52b7ed099cdc285c300001cd

def remove_overlap(ranges):
    result = []
    current_start = float('-inf')
    current_stop = float('-inf')

    for start, stop in sorted(ranges):
        if start > current_stop:
            result.append((start, stop))
            current_start, current_stop = start, stop
        else:
            current_stop = max(current_stop, stop)
            result[-1] = (current_start, current_stop)

    return result


def sum_of_intervals(intervals: list):
    x = remove_overlap(intervals)
    rob = 0
    for i in x:
        rob += (i[1] - i[0])

    return rob
