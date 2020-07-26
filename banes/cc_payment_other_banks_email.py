from typing import List
from .records import ExpenseRecord, Receiver, ExtraAmount, EXPENSE_RECORD_TYPE
from ._html_email_scrapers import banorte_email_scraper
from ._amounts import extract_amount

EMAIL_TYPE = 'CREDIT_CARD_PAYMENT_OTHER_BANKS_EMAIL'


def is_matching(html: str) -> bool:
    return 'Pago de Tarjeta de Crédito Otros Bancos' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([f.strip() for f in [fields[4], fields[18], fields[14]] if f]),
        operation_date=f'{fields[6]} {fields[8]}',
        amount=extract_amount(fields[22]),
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount=extract_amount(fields[26]),
                tax=extract_amount(fields[28]),
            ),
        ],
        receiver=Receiver(
            name=fields[16],
            bank=fields[20],
        ),
    )
