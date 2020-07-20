from baes import id_by_phone_email
from baes.records import AccountOperationRecord

EMAIL_PATH = 'identification-by-phone-email.html'


def test_is_matching(load_email):
    """it should be able to match a identification by phone email"""
    html = load_email(EMAIL_PATH)

    assert id_by_phone_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a identification by phone email"""
    html = load_email(EMAIL_PATH)
    actual = id_by_phone_email.scrape(html)
    expected = AccountOperationRecord(
        type='ACCOUNT_OPERATION',
        source='IDENTIFICATION_BY_PHONE_EMAIL',
        note='Identificacion',
        operation_date='17/12/2019 13:58',
    )

    assert actual == expected
