from banes import nip_change_email
from banes.records import AccountOperationRecord, Channel

EMAIL_PATH = 'nip-change-email.html'


def test_is_matching(load_email):
    """it should be able to match a nip change email"""
    html = load_email(EMAIL_PATH)

    assert nip_change_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a nip change email"""
    html = load_email(EMAIL_PATH)
    actual = nip_change_email.scrape(html)
    expected = AccountOperationRecord(
        type='ACCOUNT_OPERATION',
        source='NIP_CHANGE_EMAIL',
        note='CAMBIO DE NIP',
        operation_date='14/Nov 20:41:13 hrs.',
        channel=Channel(
            type='CAJERO AUTOMATICO'
        )
    )

    assert actual == expected
