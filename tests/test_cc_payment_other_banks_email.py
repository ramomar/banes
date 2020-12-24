from banes import cc_payment_other_banks_email
from banes.records import ExpenseRecord, ExtraAmount, Receiver

EMAIL_PATH = 'credit-card-payment-other-banks-email.html'


def test_is_matching(load_email):
    """it should be able to match a credit card payment other banks email"""
    html = load_email(EMAIL_PATH)

    assert cc_payment_other_banks_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a credit card payment other banks email"""
    html = load_email(EMAIL_PATH)
    actual = cc_payment_other_banks_email.scrape(html)
    expected = ExpenseRecord(
        type='EXPENSE',
        source='CREDIT_CARD_PAYMENT_OTHER_BANKS_EMAIL',
        note='Pago de Tarjeta de Crédito Otros Bancos | otro_usuario@mail.com | - ************1111',
        operation_date='27/Mar/2020 17:10:27 horas',
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount='0.00',
                tax='0.00',
            ),
        ],
        amount='2754.00',
        receiver=Receiver(
            name='OTRO USUARIO',
            bank='STP',
        ),
    )

    assert actual == expected
