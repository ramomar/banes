from banes import _amounts


def test_extract_amount_a():
    """it should be able to extract amounts like: $792.00 MN"""
    actual = _amounts.extract_amount('$792.00 MN')
    expected = '792.00'

    assert actual == expected


def test_extract_amount_b():
    """it should be able to extract amounts like: $ 63.37 MN"""
    actual = _amounts.extract_amount('$ 63.37 MN')
    expected = '63.37'

    assert actual == expected


def test_extract_amount_spei():
    """should be able to extract amounts like: 1,000.00"""
    actual = _amounts.extract_amount_spei('1,000.00')
    expected = '1000.00'

    assert actual == expected
