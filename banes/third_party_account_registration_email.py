from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'THIRD_PARTY_ACCOUNT_REGISTRATION_EMAIL'


def is_matching(html: str) -> bool:
    return 'Registro de Cuenta en catálogo de terceros Banorte' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=f'{fields[4]} | {fields[10]} | {fields[12]} | {fields[14]}',
        operation_date=f'{fields[6]} {fields[8]}',
    )
