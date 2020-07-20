from banes import spei_devolution_email
from banes.records import IncomeRecord

EMAIL_PATH = 'spei-devolution-email.html'


def test_is_matching(load_email):
    """it should be able to match a spei devolution email"""
    html = load_email(EMAIL_PATH)

    assert spei_devolution_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a spei devolution email"""
    html = load_email(EMAIL_PATH)
    actual = spei_devolution_email.scrape(html)
    note = 'Se realizo un ABONO por devolucion SPEI ' \
           'de $ 792.00 MN el 31/OCT/2019 a las 13:41:03 horas ' \
           'a la cuenta ************0000 ' \
           'Clave de Rastreo 0000AAAA000000000000000'
    expected = IncomeRecord(
        type='INCOME',
        source='SPEI_DEVOLUTION_EMAIL',
        note=note,
        operation_date='31/OCT/2019 13:41:03',
        amount='792.00',
    )

    assert actual == expected
