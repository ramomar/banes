from banes import transfer_national_banks_spei_email
from banes.records import ExpenseRecord, ExtraAmount, Receiver

EMAIL_PATH = 'transfer-national-banks-spei-email.html'


def test_is_matching(load_email):
    """it should be able to match a transfer national banks SPEI email"""
    html = load_email(EMAIL_PATH)

    assert transfer_national_banks_spei_email.is_matching(html)


def test_scrape_fast_transfer_banorte_email(load_email):
    """it should be able to scrape a transfer national banks SPEI email"""
    html = load_email(EMAIL_PATH)
    actual = transfer_national_banks_spei_email.scrape(html)
    expected = ExpenseRecord(
        type='EXPENSE',
        source='TRANSFER_NATIONAL_BANKS_SPEI_EMAIL',
        note='Transferencia a Otros Bancos Nacionales - SPEI | '
             'CUENTA ENLACE PERSONAL - *******1111 | Ana G - *******1111 | MBP',
        operation_date='12/Dic/2020 15:11:23 horas',
        amount='12000.00',
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount='3.00',
                tax='0.48',
            ),
        ],
        receiver=Receiver(
            bank='STP',
            name='Ana',
        ),
    )

    assert actual == expected
