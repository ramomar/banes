from banes import email_change_success_email
from banes.records import AccountOperationRecord, Channel, ACCOUNT_OPERATION_TYPE

EMAIL_PATH = 'email-change-success-email.html'


def test_is_matching(load_email):
    """it should be able to match an email change success email"""
    html = load_email(EMAIL_PATH)

    assert email_change_success_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape an email change success email email"""
    html = load_email(EMAIL_PATH)
    actual = email_change_success_email.scrape(html)
    expected = AccountOperationRecord(
        source='EMAIL_CHANGE_SUCCESS_EMAIL',
        type=ACCOUNT_OPERATION_TYPE,
        note='CAMBIO CORREO ELECTRONICO | EMAIL_VIEJO@EMAIL.COM | EMAIL_NUEVO@EMAIL.COM',
        operation_date='11/Dic/2020 12:00:51 hrs.',
        channel=Channel(
            type='SUCURSAL',
        ),
    )

    assert actual == expected
