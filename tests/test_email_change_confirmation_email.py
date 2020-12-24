from banes import email_change_confirmation_email
from banes.records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE

EMAIL_PATH = 'email-change-confirmation-email.html'


def test_is_matching(load_email):
    """it should be able to match a email change confirmation email"""
    html = load_email(EMAIL_PATH)

    assert email_change_confirmation_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a email change confirmation email"""
    html = load_email(EMAIL_PATH)
    actual = email_change_confirmation_email.scrape(html)
    expected = AccountOperationRecord(
        source='EMAIL_CHANGE_CONFIRMATION_EMAIL',
        type=ACCOUNT_OPERATION_TYPE,
        note='Gracias por tu preferencia, Banorte recibió una solicitud para que se asigne este correo a su cuenta, para confirmar esta solicitud favor de dar clic en el siguiente link de CONFIRMAR.  A través de mi huella dactilar ratifico que el aviso de privacidad de Banorte está disponible para mi consulta, por lo que otorgo mi consentimiento para el tratamiento de mis datos personales y datos personales sensibles (biométricos) con la finalidad de autenticarme y validar mi identidad en los canales disponibles para tal efecto.',
    )

    assert actual == expected
