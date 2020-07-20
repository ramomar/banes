from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from .html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'LIMIT_MODIFICATION_EMAIL'


def is_matching(html: str) -> bool:
    return 'Modificación de monto máximo acumulado por día' in html


@banorte_email_scraper
def scrape(rows: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=f'{rows[5]} | Monto máximo acumulado por día: {rows[13]}',
        operation_date=f'{rows[7]} {rows[9]}',
    )
