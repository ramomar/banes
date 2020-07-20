from banes import deposit_email
from banes.records import ExpenseRecord, Receiver

EMAIL_PATH = 'deposit-email.html'


def test_is_matching(load_email):
    """it should be able to match a deposit email"""
    html = load_email(EMAIL_PATH)

    assert deposit_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a deposit email"""
    html = load_email(EMAIL_PATH)
    actual = deposit_email.scrape(html)
    expected = ExpenseRecord(
        type='EXPENSE',
        source='DEPOSIT_EMAIL',
        note='Instrucción de Depósito | Pago del cine',
        operation_date='31/Oct/2019 13:41:03 horas',
        amount='792.00',
        receiver=Receiver(
            name='USUARIO BBVA BANCOMER',
            bank='BBVA BANCOMER',
        ),
    )

    assert actual == expected
