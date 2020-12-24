from banes import cc_payment_third_parties
from banes.records import ExpenseRecord, ExtraAmount, Receiver

EMAIL_PATH = 'credit-card-payment-third-parties-email.html'


def test_is_matching(load_email):
    """it should be able to match a credit card payment third parties email"""
    html = load_email(EMAIL_PATH)

    assert cc_payment_third_parties.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a credit card payment third parties email"""
    html = load_email(EMAIL_PATH)
    actual = cc_payment_third_parties.scrape(html)
    expected = ExpenseRecord(
        type='EXPENSE',
        source='CREDIT_CARD_PAYMENT_THIRD_PARTIES_EMAIL',
        note='Pago de Tarjeta de Crédito Terceros | otro_usuario@mail.com | ************1234 | - ************2222',
        operation_date='20/Ago/2020 19:49:10 horas',
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount='0.00',
                tax='0.00',
            ),
        ],
        amount='1.00',
        receiver=Receiver(
            name='OTRO USUARIO',
            bank='Nu',
        ),
    )

    assert actual == expected
