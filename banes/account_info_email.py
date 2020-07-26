from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'ACCOUNT_INFO_EMAIL'


def is_matching(html: str) -> bool:
    return 'Informacion de tu Cuenta' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=fields[5],
        operation_date=fields[15],
    )
