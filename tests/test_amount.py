from baes import amount


def test_extract_amount_a():
    """it should be able to extract amounts like: $792.00 MN"""
    actual = amount.extract_amount('$792.00 MN')
    expected = '792.00'

    assert actual == expected
