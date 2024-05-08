# https://www.codewars.com/kata/550f22f4d758534c1100025a

def dir_reduc(arr):
    opposite_map = {'NORTH': 'SOUTH',
                    'SOUTH': 'NORTH',
                    'WEST': 'EAST',
                    'EAST': 'WEST'
                    }

    while True:
        current = len(arr)
        for k, v in enumerate(arr):
            if k == len(arr)-1:
                continue
            if arr[k+1] == opposite_map[v]:
                del arr[k+1], arr[k]
                continue
        new = len(arr)
        if current == new:
            break
    return arr


a = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']
print(dir_reduc(a))  # ['WEST']
