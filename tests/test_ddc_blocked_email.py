from banes import ddc_blocked_email
from banes.records import AccountOperationRecord

EMAIL_PATH = 'digital-debit-card-blocked-email.html'


def test_is_matching(load_email):
    """it should be able to match a digital debit card blocked email"""
    html = load_email(EMAIL_PATH)

    assert ddc_blocked_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a digital debit card blocked email"""
    html = load_email(EMAIL_PATH)
    actual = ddc_blocked_email.scrape(html)
    expected = AccountOperationRecord(
        type='ACCOUNT_OPERATION',
        source='DIGITAL_DEBIT_CARD_BLOCKED_EMAIL',
        note='Bloqueo de Tarjeta Digital de Débito | CUENTA ENLACE PERSONAL ****0000',
        operation_date='22/Ago/2019 20:28:59 horas',
    )

    assert actual == expected
