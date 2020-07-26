from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'DEBIT_CARD_BLOCKED_EMAIL'


def is_matching(html: str) -> bool:
    return 'Bloqueo de Tarjeta de Débito' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([r.strip() for r in [fields[5], fields[11]] if r]),
        operation_date=f'{fields[7]} {fields[9]}',
    )
