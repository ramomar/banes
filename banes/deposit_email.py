from typing import List
from .records import ExpenseRecord, Receiver, EXPENSE_RECORD_TYPE
from ._html_email_scrapers import banorte_email_scraper
from ._amounts import extract_amount

EMAIL_TYPE = 'DEPOSIT_EMAIL'


def is_matching(html: str) -> bool:
    return 'Instrucción de Depósito' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([f.strip() for f in [fields[4], fields[18]] if f]),
        operation_date=f'{fields[6]} {fields[8]}',
        amount=extract_amount(fields[16]),
        receiver=Receiver(
            name=fields[10],
            bank=fields[14],
        ),
    )
