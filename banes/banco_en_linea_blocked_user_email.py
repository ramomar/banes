from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'BANCO_EN_LINEA_BLOCKED_USER_EMAIL'


def is_matching(html: str) -> bool:
    return 'Bloqueo de usuario' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        source=EMAIL_TYPE,
        type=ACCOUNT_OPERATION_TYPE,
        note=f'{fields[14]} | Token: {fields[10]}',
        operation_date=f'{fields[6]} {fields[8].strip()}',
    )
