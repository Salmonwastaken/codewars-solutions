import pytest

from sum_of_intervals import sum_of_intervals


@pytest.mark.parametrize("input, output",
                         [
                            ([(1, 5)], 4),
                            ([(1, 5), (6, 10)], 8),
                            ([(1, 5), (1, 5)], 4),
                            ([(1, 4), (7, 10), (3, 5)], 7),
                            ([(-1_000_000_000, 1_000_000_000)], 2_000_000_000),
                            ([(0, 20), (-100_000_000, 10), (30, 40)], 100_000_030),
                            ([(-439, -345), (251, 420), (256, 267), (-141, -118), (-310, 61), (293, 444)], 658)
                         ])
def test_permutation(input, output):
    assert sum_of_intervals(input) == output
