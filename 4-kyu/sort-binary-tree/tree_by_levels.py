# https://www.codewars.com/kata/52bef5e3588c56132c0003bc

def tree_by_levels(tree):
    if tree is None:
        return []

    queue = []
    result = []
    queue.append(tree)

    while (len(queue) > 0):
        result.append(queue[0].value)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return result