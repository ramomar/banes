from banes import banorte_movil_activation_email
from banes.records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE

EMAIL_PATH = 'banorte-movil-activation-email.html'


def test_is_matching(load_email):
    """it should be able to match a banorte movil activation email"""
    html = load_email(EMAIL_PATH)

    assert banorte_movil_activation_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a banorte movil activation email"""
    html = load_email(EMAIL_PATH)
    actual = banorte_movil_activation_email.scrape(html)
    expected = AccountOperationRecord(
        source='BANORTE_MOVIL_ACTIVATION_EMAIL',
        type=ACCOUNT_OPERATION_TYPE,
        note='Activación de Banorte Móvil',
        operation_date='11/Dic/2020 12:14:47'
    )

    assert actual == expected
