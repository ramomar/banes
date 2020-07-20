from baes import limit_modification_email
from baes.records import AccountOperationRecord

EMAIL_PATH = 'limit-modification-email.html'


def test_is_matching(load_email):
    """it should be able to match a limit modification email"""
    html = load_email(EMAIL_PATH)

    assert limit_modification_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a limit modification email"""
    html = load_email(EMAIL_PATH)
    actual = limit_modification_email.scrape(html)
    expected = AccountOperationRecord(
        type='ACCOUNT_OPERATION',
        source='LIMIT_MODIFICATION_EMAIL',
        note='Modificación de monto máximo acumulado por día. | Monto máximo acumulado por día: $1,000.00 MN',
        operation_date='20/May/2019 18:42:40 horas',
    )

    assert actual == expected
