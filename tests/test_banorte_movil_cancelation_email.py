from banes import banorte_movil_cancelation_email
from banes.records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE

EMAIL_PATH = 'banorte-movil-cancelation-email.html'


def test_is_matching(load_email):
    """it should be able to match a banorte movil activation email"""
    html = load_email(EMAIL_PATH)

    assert banorte_movil_cancelation_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a banorte movil activation email"""
    html = load_email(EMAIL_PATH)
    actual = banorte_movil_cancelation_email.scrape(html)
    expected = AccountOperationRecord(
        source='BANORTE_MOVIL_CANCELATION_EMAIL',
        type=ACCOUNT_OPERATION_TYPE,
        note='Tu servicio ha sido cancelado exitosamente. | ************1111 | 0000000000',
        operation_date='11Dic/2020 10:50:49 hrs.'
    )

    assert actual == expected
