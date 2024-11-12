import pytest


def add_two_numbers(a, b):

    return a + b


MSG = 'The sum of {} and {} should be {}'

@pytest.mark.math
def test_small_numbers():

    a, b, c = 1, 2, 3
    assert add_two_numbers(a, b) == c, MSG.format(a, b, c)


@pytest.mark.math
def test_large_numbers():

    a, b, c = 100, 300, 400
    assert add_two_numbers(a, b) == c, MSG.format(a, b, c)

