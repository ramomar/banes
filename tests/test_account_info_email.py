from baes import account_info_email
from baes.record import AccountOperationRecord

EMAIL_PATH = 'account-info-email.html'


def test_is_matching(load_email):
    """it should be able to match an account info email"""
    html = load_email(EMAIL_PATH)

    assert account_info_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape an account info email"""
    html = load_email(EMAIL_PATH)
    actual = account_info_email.scrape(html)
    expected = AccountOperationRecord(
        type='ACCOUNT_OPERATION',
        source='ACCOUNT_INFO_EMAIL',
        note='Informacion de tu Cuenta',
        operation_date='17/12/2019 13:58',
    )

    assert actual == expected
