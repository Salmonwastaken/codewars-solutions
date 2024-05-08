# https://www.codewars.com/kata/576757b1df89ecf5bd00073b
# Apparently `.center` exists, whoops

def tower_builder(n):

    tower = []

    total = 2 * (n - 1) + 1

    current = total
    for i in range(n):
        size = int(((total - current) / 2))
        layer = f'{size * " "}{current * "*"}{size * " "}'
        tower.append(layer)
        current -= 2
    tower.reverse()
    return tower


print(tower_builder(3))
# print(tower_builder(6))
