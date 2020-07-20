from typing import List
from .records import ExpenseRecord, Channel, EXPENSE_RECORD_TYPE
from .html_email_scrapers import banorte_email_scraper
from .amounts import extract_amount

EMAIL_TYPE = 'SERVICE_PAYMENT_EMAIL'


def is_matching(html: str) -> bool:
    return 'PAGO DE SERVICIOS' in html


@banorte_email_scraper
def scrape(rows: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=rows[4],
        operation_date=rows[6].replace(r'\s+', ' '),
        application_date=rows[8],
        channel=Channel(
            type=rows[18],
        ),
        amount=extract_amount(rows[12]),
    )

