from baes import fast_transfer_email
from baes.record import ExpenseRecord, ExtraAmount, Receiver

FAST_TRANSFER_BANORTE_EMAIL_PATH = 'fast-transfer-banorte-email.html'
FAST_TRANSFER_OTHER_BANKS_EMAIL_PATH = 'fast-transfer-other-banks-email.html'


def test_is_matching_fast_transfer_banorte_email(load_email):
    """it should be able to match a transfer for banorte email"""
    html = load_email(FAST_TRANSFER_BANORTE_EMAIL_PATH)

    assert fast_transfer_email.is_matching(html)


def test_is_matching_fast_transfer_other_banks_email(load_email):
    """it should be able to match a transfer for banorte email"""
    html = load_email(FAST_TRANSFER_OTHER_BANKS_EMAIL_PATH)

    assert fast_transfer_email.is_matching(html)


def test_scrape_fast_transfer_banorte_email(load_email):
    """it should be able to scrape an email for a transfer to a banorte account"""
    html = load_email(FAST_TRANSFER_BANORTE_EMAIL_PATH)
    actual = fast_transfer_email.scrape(html)
    expected = ExpenseRecord(
        type='EXPENSE',
        source='FAST_TRANSFER_EMAIL',
        note='Transferencias Rápidas | Cosas | beneficiario@mail.com',
        operation_date='21/Oct/2019 11:23:02 horas',
        amount='600.00',
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount='0.00',
                tax='0.00'
            )
        ],
        receiver=Receiver(
            bank='Banorte',
            name='No capturado',
        ),
    )

    assert actual == expected


def test_scrape_fast_transfer_other_banks_email(load_email):
    """it should be able to scrape an email for a transfer to another bank"""
    html = load_email(FAST_TRANSFER_OTHER_BANKS_EMAIL_PATH)
    actual = fast_transfer_email.scrape(html)
    expected = ExpenseRecord(
        type='EXPENSE',
        source='FAST_TRANSFER_EMAIL',
        note='Transferencias Rápidas | Open source | hola@github.com',
        operation_date='03/Ago/2019 11:13:14 horas',
        amount='806.00',
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount='3.00',
                tax='0.48'
            )
        ],
        receiver=Receiver(
            bank='BBVA BANCOMER',
            name='GitHub',
        ),
    )

    assert actual == expected
