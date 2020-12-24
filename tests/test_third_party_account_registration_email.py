from banes import third_party_account_registration_email
from banes.records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE

EMAIL_PATH = 'third-party-account-registration-email.html'


def test_is_matching(load_email):
    """it should be able to match a third party account registration email"""
    html = load_email(EMAIL_PATH)

    assert third_party_account_registration_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a third party account registration email"""
    html = load_email(EMAIL_PATH)
    actual = third_party_account_registration_email.scrape(html)
    expected = AccountOperationRecord(
        source='THIRD_PARTY_ACCOUNT_REGISTRATION_EMAIL',
        type=ACCOUNT_OPERATION_TYPE,
        note='Registro de Cuenta en catálogo de terceros Banorte | Ana Nu | *******1111 | STP',
        operation_date='12-Dic-2020 02:48:32 horas',
    )

    assert actual == expected
