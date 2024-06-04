import pytest

from permutations import permutations


@pytest.mark.parametrize("input, output",
                         [
                            ('a', ['a']),
                            ('ab', ['ab', 'ba'])
                         ])
def test_permutation(input, output):
    assert permutations(input) == output
