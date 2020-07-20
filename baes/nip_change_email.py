from typing import List
from .records import AccountOperationRecord, Channel, ACCOUNT_OPERATION_TYPE
from .html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'NIP_CHANGE_EMAIL'


def is_matching(html: str) -> bool:
    return 'CAMBIO DE NIP' in html


@banorte_email_scraper
def scrape(rows: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=rows[12],
        operation_date=rows[4],
        channel=Channel(
            type=rows[14],
        ),
    )
