from banes import cash_withdrawal_alt_email
from banes.records import ExpenseRecord, Channel

EMAIL_PATH = 'cash-withdrawal-alt-email.html'


def test_is_matching(load_email):
    """it should be able to match a cash withdrawal alt email"""
    html = load_email(EMAIL_PATH)

    assert cash_withdrawal_alt_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a cash withdrawal alt email"""
    html = load_email(EMAIL_PATH)
    actual = cash_withdrawal_alt_email.scrape(html)
    expected = ExpenseRecord(
        type='EXPENSE',
        source='CASH_WITHDRAWAL_ALT_EMAIL',
        note='DISPOSICION DE EFECTIVO',
        operation_date='14/May 20:15:31 hrs.',
        application_date='14/May/2019',
        channel=Channel(
            type='CAJERO VISA NET',
        ),
        amount='337.88',
    )

    assert actual == expected
