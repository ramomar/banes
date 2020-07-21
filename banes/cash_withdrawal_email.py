from typing import List
from .records import ExpenseRecord, Channel, ChannelDetails, EXPENSE_RECORD_TYPE
from .html_email_scrapers import banorte_email_scraper
from .amounts import extract_amount

EMAIL_TYPE = 'CASH_WITHDRAWAL_EMAIL'


def is_matching(html: str) -> bool:
    return 'RETIRO DE EFECTIVO' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=fields[5],
        operation_date=fields[7],
        application_date=fields[9],
        channel=Channel(
            type=fields[23],
            details=ChannelDetails(
                name=fields[21],
                location=fields[25],
            ),
        ),
        amount=extract_amount(fields[27]),
    )
