from baes import phone_recharge_email
from baes.records import ExpenseRecord

EMAIL_PATH = 'phone-recharge-email.html'


def test_is_matching(load_email):
    """it should be able to match a phone recharge email"""
    html = load_email(EMAIL_PATH)

    assert phone_recharge_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a phone recharge email"""
    html = load_email(EMAIL_PATH)
    actual = phone_recharge_email.scrape(html)
    expected = ExpenseRecord(
        type='EXPENSE',
        source='PHONE_RECHARGE_EMAIL',
        note='Compra de Tiempo Aire/Paquetes Sin Límite | 0000000000',
        operation_date='01/Oct/2019 15:08:52 horas',
        amount='200.00',
    )

    assert actual == expected
