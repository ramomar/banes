from typing import List
import re
from .records import ExpenseRecord, EXPENSE_RECORD_TYPE
from .html_email_scrapers import banorte_email_scraper
from .amounts import extract_amount

EMAIL_TYPE = 'PHONE_RECHARGE_EMAIL'


def is_matching(html: str) -> bool:
    return 'Compra de Tiempo Aire' in html


@banorte_email_scraper
def scrape(rows: List[str]) -> ExpenseRecord:
    phone = re.search(r'\d+', rows[14])[0]  # type: ignore

    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([r.strip() for r in [rows[4], phone] if r]),
        operation_date=f'{rows[6]} {rows[8]}',
        amount=extract_amount(rows[18]),
    )

