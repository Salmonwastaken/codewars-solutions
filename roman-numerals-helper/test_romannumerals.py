from romannumerals import RomanNumerals


def do_test(input, expected):
    func = RomanNumerals.to_roman if type(input) is int else RomanNumerals.from_roman
    actual = func(input)
    assert actual == expected


def test_to():
    do_test(1000, 'M')
    do_test(4, 'IV')
    do_test(1, 'I')
    do_test(1990, 'MCMXC')
    do_test(2008, 'MMVIII')


def test_from():
    do_test('XXI', 21)
    do_test('I', 1)
    do_test('IV', 4)
    do_test('MMVIII', 2008)
    do_test('MDCLXVI', 1666)
