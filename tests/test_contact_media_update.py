from banes import contact_media_update_email
from banes.records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE

EMAIL_PATH = 'contact-media-update-email.html'


def test_is_matching(load_email):
    """it should be able to match a contact media update email"""
    html = load_email(EMAIL_PATH)

    assert contact_media_update_email.is_matching(html)


def test_scrape(load_email):
    """it should be able to scrape a contact media update email"""
    html = load_email(EMAIL_PATH)
    actual = contact_media_update_email.scrape(html)
    expected = AccountOperationRecord(
        source='CONTACT_MEDIA_UPDATE_EMAIL',
        type=ACCOUNT_OPERATION_TYPE,
        note='Actualización de Medios de Contacto | email_viejo@email.com | email_nuevo@email.com',
        operation_date='01/Dec/2020 19:14:43 horas',
    )

    assert actual == expected
