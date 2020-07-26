from typing import List
import re
from .records import ExpenseRecord, EXPENSE_RECORD_TYPE
from ._html_email_scrapers import banorte_email_scraper
from ._amounts import extract_amount

EMAIL_TYPE = 'PHONE_RECHARGE_EMAIL'


def is_matching(html: str) -> bool:
    return 'Compra de Tiempo Aire' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> ExpenseRecord:
    phone = re.search(r'\d+', fields[14])[0]  # type: ignore

    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([f.strip() for f in [fields[4], phone] if f]),
        operation_date=f'{fields[6]} {fields[8]}',
        amount=extract_amount(fields[18]),
    )
