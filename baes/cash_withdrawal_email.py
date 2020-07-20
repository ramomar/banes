from typing import List
from .record import ExpenseRecord, Channel, ChannelDetails, EXPENSE_RECORD_TYPE
from .scraper import banorte_email_scraper
from .amount import extract_amount

EMAIL_TYPE = 'CASH_WITHDRAWAL_EMAIL'


def is_matching(html: str) -> bool:
    return 'RETIRO DE EFECTIVO' in html


@banorte_email_scraper
def scrape(rows: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=rows[5],
        operation_date=rows[7],
        application_date=rows[9],
        channel=Channel(
            type=rows[23],
            details=ChannelDetails(
                name=rows[21],
                location=rows[25],
            ),
        ),
        amount=extract_amount(rows[27]),
    )
