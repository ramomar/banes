from typing import List
from .records import AccountOperationRecord, Channel, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'NIP_CHANGE_EMAIL'


def is_matching(html: str) -> bool:
    return 'CAMBIO DE NIP' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=fields[12],
        operation_date=fields[4],
        channel=Channel(
            type=fields[14],
        ),
    )
