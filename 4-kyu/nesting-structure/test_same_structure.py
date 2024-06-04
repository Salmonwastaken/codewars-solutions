import pytest

from same_structure import same_structure_as


@pytest.mark.parametrize("original, other, answer",
                         [
                            ([1, [1, 1]], [2, [2, 2]], True),
                            ([1, [1, 1]], [[2, 2], 2], False),
                            ([1, [1, 1]], [2, [2]], False),
                            ([[[], []]], [[[], []]], True),
                            ([1, '[', ']'], ['[', ']', 1], True)
                         ])
def test_structure(original, other, answer):
    assert same_structure_as(original, other) == answer
