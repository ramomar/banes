from typing import List
from .records import ExpenseRecord, ExtraAmount, Receiver, EXPENSE_RECORD_TYPE
from ._html_email_scrapers import banorte_email_scraper
from ._amounts import extract_amount

EMAIL_TYPE = 'TRANSFER_THIRD_PARTY_EMAIL'


def is_matching(html: str) -> bool:
    return 'Transferencias a Cuentas de Terceros' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([f.strip() for f in [fields[4], fields[10], fields[12], fields[32]] if f]),
        operation_date=f'{fields[6]} {fields[8]}',
        amount=extract_amount(fields[22]),
        extra_amounts=[
            ExtraAmount(
                name='tax',
                amount=extract_amount(fields[24]),
                tax='0.00'
            ),
            ExtraAmount(
                name='fee',
                amount=extract_amount(fields[26]),
                tax=extract_amount(fields[28]),
            ),
        ],
        receiver=Receiver(
            bank=fields[20],
            name=fields[14],
        ),
    )
