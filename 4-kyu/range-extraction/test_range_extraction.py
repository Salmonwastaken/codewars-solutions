import pytest

from range_extraction import solution


@pytest.mark.parametrize("args, answer",
                         [
                            ([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20], "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"),
                            ([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20], "-6,-3-1,3-5,7-11,14,15,17-20"),
                            ([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20], "-3--1,2,10,15,16,18-20")
                         ])
def test_structure(args, answer):
    assert solution(args) == answer
