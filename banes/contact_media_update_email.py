from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'CONTACT_MEDIA_UPDATE_EMAIL'


def is_matching(html: str) -> bool:
    return 'Actualización de Medios de Contacto' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=f'{fields[3]} | {fields[9]} | {fields[11]}',
        operation_date=f'{fields[5]} {fields[7]}',
    )
