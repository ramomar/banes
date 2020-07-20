from banes import cash_withdrawal_email
from banes.records import ExpenseRecord, Channel, ChannelDetails

EMAIL_PATH = 'cash-withdrawal-email.html'


def test_is_matching(load_email):
    """it should be able to match a cash withdrawal email"""
    html = load_email(EMAIL_PATH)

    assert cash_withdrawal_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a cash withdrawal email"""
    html = load_email(EMAIL_PATH)
    actual = cash_withdrawal_email.scrape(html)
    expected = ExpenseRecord(
        type='EXPENSE',
        source='CASH_WITHDRAWAL_EMAIL',
        note='RETIRO DE EFECTIVO',
        operation_date='04/Oct/2019 14:26:15 horas',
        application_date='04/Oct/2019',
        channel=Channel(
            type='Cajero Banorte',
            details=ChannelDetails(
                name='CAJERO EN ALGUN LUGAR',
                location='UNA CIUDAD'
            ),
        ),
        amount='100.00'
    )

    assert actual == expected
