from baes import dc_blocked_email
from baes.records import AccountOperationRecord

EMAIL_PATH = 'debit-card-blocked-email.html'


def test_is_matching(load_email):
    """it should be able to match a debit card blocked email"""
    html = load_email(EMAIL_PATH)

    assert dc_blocked_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a debit card blocked email"""
    html = load_email(EMAIL_PATH)
    actual = dc_blocked_email.scrape(html)
    expected = AccountOperationRecord(
        type='ACCOUNT_OPERATION',
        source='DEBIT_CARD_BLOCKED_EMAIL',
        note='Bloqueo de Tarjeta de Débito | Cuenta Enlace Personal - ************0000',
        operation_date='12/Nov/2019 08:56:50 horas',
    )

    assert actual == expected
