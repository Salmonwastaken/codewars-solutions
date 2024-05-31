from tree_by_levels import tree_by_levels
import pytest


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


buh = Node(L=Node(L=None, R=Node(L=None, R=None, n=4), n=2), R=Node(L=Node(L=None, R=None, n=5), R=Node(L=None, R=None, n=6), n=3), n=1)


@pytest.mark.parametrize("node, expected",
                         [
                            (Node(L=Node(L=None, R=Node(L=None, R=None, n=4), n=2), R=Node(L=Node(L=None, R=None, n=5), R=Node(L=None, R=None, n=6), n=3), n=1), [1, 2, 3, 4, 5, 6]),
                            (None, [])
                         ],)
def test_tree(node, expected):
    assert tree_by_levels(node) == expected
