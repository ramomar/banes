from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'DIGITAL_DEBIT_CARD_ACTIVATED_EMAIL'


def is_matching(html: str) -> bool:
    return 'Activación de Tarjeta Digital asociada a tu Cuenta de Débito' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=f'{fields[5]} | {fields[11]}',
        operation_date=f'{fields[7]} {fields[9]}',
    )
