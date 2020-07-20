from banes import service_payment_email
from banes.records import ExpenseRecord, Channel

EMAIL_PATH = 'service-payment-email.html'


def test_is_matching(load_email):
    """it should be able to match a service payment email"""
    html = load_email(EMAIL_PATH)

    assert service_payment_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a service payment email"""
    html = load_email(EMAIL_PATH)
    actual = service_payment_email.scrape(html)
    expected = ExpenseRecord(
        type='EXPENSE',
        source='SERVICE_PAYMENT_EMAIL',
        note='PAGO DE SERVICIOS',
        operation_date='27/Nov 17:07:03 hrs.',
        application_date='27/Nov/2019',
        amount='4000.00',
        channel=Channel(
            type='CAJERO BANORTE',
        ),
    )

    assert actual == expected
