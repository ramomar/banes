from typing import List
from .records import ExpenseRecord, ExtraAmount, Receiver, EXPENSE_RECORD_TYPE
from ._html_email_scrapers import banorte_email_scraper
from ._amounts import extract_amount

EMAIL_TYPE = 'TRANSFER_NATIONAL_BANKS_SPEI_EMAIL'


def is_matching(html: str) -> bool:
    return 'Transferencia a Otros Bancos Nacionales - SPEI' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([f.strip() for f in [fields[4], fields[10], fields[16], fields[36]] if f]),
        operation_date=f'{fields[6]} {fields[8]}',
        amount=extract_amount(fields[26]),
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount=extract_amount(fields[30]),
                tax=extract_amount(fields[32]),
            ),
        ],
        receiver=Receiver(
            bank=fields[24],
            name=fields[18],
        ),
    )
