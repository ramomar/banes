from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from .html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'IDENTIFICATION_BY_PHONE_EMAIL'


def is_matching(html: str) -> bool:
    return 'Menú Telefónico Banorte' in html and 'Identificacion' in html


@banorte_email_scraper
def scrape(rows: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=rows[5],
        operation_date=rows[17],
    )