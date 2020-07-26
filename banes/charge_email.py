from typing import List
from .records import ExpenseRecord, Channel, EXPENSE_RECORD_TYPE
from ._html_email_scrapers import banorte_email_scraper
from ._amounts import extract_amount

EMAIL_TYPE = 'CHARGE_EMAIL'


def is_matching(html: str) -> bool:
    return 'COMPRA EN' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=fields[4],
        operation_date=fields[6].replace(r'\s+', ' '),
        application_date=fields[8],
        channel=Channel(
            type=fields[16],
        ),
        amount=extract_amount(fields[12]),
    )
