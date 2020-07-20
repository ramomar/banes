from typing import List
from .record import ExpenseRecord, Channel, EXPENSE_RECORD_TYPE
from .scraper import banorte_email_scraper
from .amount import extract_amount

EMAIL_TYPE = 'CHARGE_EMAIL'


def is_matching(html: str) -> bool:
    return 'COMPRA EN' in html


@banorte_email_scraper
def scrape(rows: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=rows[4],
        operation_date=rows[6].replace(r'\s+', ' '),
        application_date=rows[8],
        channel=Channel(
            type=rows[16],
        ),
        amount=extract_amount(rows[12]),
    )

