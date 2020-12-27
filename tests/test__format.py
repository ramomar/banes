from banes import _format


def test__remove_extra_whitespaces():
    expected = 'hola hola hola hola'
    actual = _format.remove_extra_whitespaces('hola  hola hola  hola')

    assert actual == expected
