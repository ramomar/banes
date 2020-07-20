from baes import charge_email
from baes.records import ExpenseRecord, Channel

EMAIL_PATH = 'charge-email.html'


def test_is_matching(load_email):
    """it should be able to match a charge email"""
    html = load_email(EMAIL_PATH)

    assert charge_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a charge email email"""
    html = load_email(EMAIL_PATH)
    actual = charge_email.scrape(html)
    expected = ExpenseRecord(
        type='EXPENSE',
        source='CHARGE_EMAIL',
        note='COMPRA EN UBER TRIP HELP.UBER.CO',
        operation_date='10/Feb 08:14:03 hrs.',
        application_date='10/Feb/2020',
        channel=Channel(
            type='TPV(COMPRA COMERCIO)',
        ),
        amount='63.37',
    )

    assert actual == expected
