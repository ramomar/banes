from banes import transfer_third_party_email
from banes.records import ExpenseRecord, ExtraAmount, Receiver

EMAIL_PATH = 'transfer-third-party-email.html'


def test_is_matching(load_email):
    """it should be able to match a transfer third party email"""
    html = load_email(EMAIL_PATH)

    assert transfer_third_party_email.is_matching(html)


def test_scrape_transfer_third_party_email(load_email):
    """it should be able to scrape a transfer third party email"""
    html = load_email(EMAIL_PATH)
    actual = transfer_third_party_email.scrape(html)
    expected = ExpenseRecord(
        type='EXPENSE',
        source='TRANSFER_THIRD_PARTY_EMAIL',
        note='Transferencias a Cuentas de Terceros | '
             'CUENTA ENLACE PERSONAL - *******1111 | Ana - *******7777 | A - 112',
        operation_date='22/Feb/2021 19:06:53 horas',
        amount='1000.00',
        extra_amounts=[
            ExtraAmount(
                name='tax',
                amount='0.00',
                tax='0.00',
            ),
            ExtraAmount(
                name='fee',
                amount='0.00',
                tax='0.00',
            ),
        ],
        receiver=Receiver(
            bank='Banorte',
            name='Ana',
        ),
    )

    assert actual == expected
