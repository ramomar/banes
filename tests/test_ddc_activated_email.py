from banes import ddc_activated_email
from banes.records import AccountOperationRecord

EMAIL_PATH = 'digital-debit-card-activated-email.html'


def test_is_matching(load_email):
    """it should be able to match a digital debit card activated email"""
    html = load_email(EMAIL_PATH)

    assert ddc_activated_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a digital debit card activated email"""
    html = load_email(EMAIL_PATH)
    actual = ddc_activated_email.scrape(html)
    expected = AccountOperationRecord(
        type='ACCOUNT_OPERATION',
        source='DIGITAL_DEBIT_CARD_ACTIVATED_EMAIL',
        note='Activación de Tarjeta Digital asociada a tu Cuenta de Débito | CUENTA ENLACE PERSONAL ****0000',
        operation_date='25/Ago/2019 13:07:48 horas',
    )

    assert actual == expected
