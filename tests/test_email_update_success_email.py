from banes import email_update_success_email
from banes.records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE

EMAIL_PATH = 'email-update-success-email.html'


def test_is_matching(load_email):
    """it should be able to match an email update success email"""
    html = load_email(EMAIL_PATH)

    assert email_update_success_email.is_matching(html)


def test_is_matching_crlf(load_email):
    """it should be able to match an email update success email when linebreaks are encoded with CRLF"""
    html = load_email('email-update-success-email-crlf.html')

    assert email_update_success_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape an email update success email"""
    html = load_email(EMAIL_PATH)
    actual = email_update_success_email.scrape(html)
    expected = AccountOperationRecord(
        source='EMAIL_UPDATE_SUCCESS_EMAIL',
        type=ACCOUNT_OPERATION_TYPE,
        note='Le notificamos que la actualizacion de su correo electronico ha finalizado con exito',
        operation_date='01/Dic/2020 19:14:42 hrs.',
    )

    assert actual == expected
