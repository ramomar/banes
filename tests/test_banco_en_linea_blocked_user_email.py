from banes import banco_en_linea_blocked_user_email
from banes.records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE

EMAIL_PATH = 'banco-en-linea-blocked-user-email.html'


def test_is_matching(load_email):
    """it should be able to match a banco en linea blocked user email"""
    html = load_email(EMAIL_PATH)

    assert banco_en_linea_blocked_user_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a banco en linea blocked user email"""
    html = load_email(EMAIL_PATH)
    actual = banco_en_linea_blocked_user_email.scrape(html)
    expected = AccountOperationRecord(
        source='BANCO_EN_LINEA_BLOCKED_USER_EMAIL',
        type=ACCOUNT_OPERATION_TYPE,
        note='Error al capturar token o contraseña incorrecta | Token: ******1020',
        operation_date='07/Ene/2021 15:04 horas',
    )

    assert actual == expected
