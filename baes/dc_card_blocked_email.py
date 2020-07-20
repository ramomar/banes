from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from .scraper import banorte_email_scraper

EMAIL_TYPE = 'DEBIT_CARD_BLOCKED_EMAIL'


def is_matching(html: str) -> bool:
    return 'Bloqueo de Tarjeta de Débito' in html


@banorte_email_scraper
def scrape(rows: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([r.strip() for r in [rows[5], rows[11]] if r]),
        operation_date=f'{rows[7]} {rows[9]}',
    )
