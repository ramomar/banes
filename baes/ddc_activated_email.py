from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from .html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'DIGITAL_DEBIT_CARD_ACTIVATED_EMAIL'


def is_matching(html: str) -> bool:
    return 'Activación de Tarjeta Digital asociada a tu Cuenta de Débito' in html


@banorte_email_scraper
def scrape(rows: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=f'{rows[5]} | {rows[11]}',
        operation_date=f'{rows[7]} {rows[9]}',
    )
