from banes import notification_medium_change_email
from banes.records import AccountOperationRecord, Channel, ACCOUNT_OPERATION_TYPE

EMAIL_PATH = 'notification-medium-change-email.html'


def test_is_matching(load_email):
    """it should be able to match an email change success email"""
    html = load_email(EMAIL_PATH)

    assert notification_medium_change_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape an email change success email email"""
    html = load_email(EMAIL_PATH)
    actual = notification_medium_change_email.scrape(html)
    expected = AccountOperationRecord(
        source='NOTIFICATION_MEDIUM_CHANGE_EMAIL',
        type=ACCOUNT_OPERATION_TYPE,
        note='CAMBIO CORREO ELECTRONICO | EMAIL_VIEJO@EMAIL.COM | EMAIL_NUEVO@EMAIL.COM',
        operation_date='11/Dic/2020 12:00:51 hrs.',
        channel=Channel(
            type='SUCURSAL',
        ),
    )

    assert actual == expected
