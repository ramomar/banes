from typing import List
from .record import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from .scraper import banorte_email_scraper

EMAIL_TYPE = 'ACCOUNT_INFO_EMAIL'


def is_matching(html: str) -> bool:
    return 'Informacion de tu Cuenta' in html


@banorte_email_scraper
def scrape(rows: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=rows[5],
        operation_date=rows[15],
    )
