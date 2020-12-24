from typing import List
from .records import ExpenseRecord, Receiver, ExtraAmount, EXPENSE_RECORD_TYPE
from ._html_email_scrapers import banorte_email_scraper
from ._amounts import extract_amount

EMAIL_TYPE = 'CREDIT_CARD_PAYMENT_THIRD_PARTIES_EMAIL'


def is_matching(html: str) -> bool:
    return 'Pago de Tarjeta de Crédito Terceros' in html or 'Pago de Tarjeta de Crédito Terceros' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> ExpenseRecord:
    print(fields)
    for f in enumerate(fields):
        print(f)
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([f.strip() for f in [fields[3].replace(' ', ' '), fields[19], fields[11], fields[13]] if f]),
        operation_date=f'{fields[5]} {fields[7]}',
        amount=extract_amount(fields[21]),
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount=extract_amount(fields[25]),
                tax=extract_amount(fields[27]),
            ),
        ],
        receiver=Receiver(
            name=fields[17],
            bank=fields[15],
        ),
    )
