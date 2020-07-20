from banes import spei_income_email
from banes.records import IncomeRecord

EMAIL_PATH = 'spei-income-email.html'


def test_is_matching(load_email):
    """it should be able to match a spei income email"""
    html = load_email(EMAIL_PATH)

    assert spei_income_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a spei income email"""
    html = load_email(EMAIL_PATH)
    actual = spei_income_email.scrape(html)
    expected = IncomeRecord(
        type='INCOME',
        source='SPEI_INCOME_EMAIL',
        note='Se realizo un ABONO SPEI de $ 1,000.00 MN el 28/MAY/2019 a las 13:41:34',
        operation_date='28/MAY/2019 13:41:34',
        amount='1000.00',
    )

    assert actual == expected
