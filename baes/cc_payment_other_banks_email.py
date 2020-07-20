from typing import List
from .records import ExpenseRecord, Receiver, ExtraAmount, EXPENSE_RECORD_TYPE
from .scraper import banorte_email_scraper
from .amounts import extract_amount

EMAIL_TYPE = 'CREDIT_CARD_PAYMENT_OTHER_BANKS_EMAIL'


def is_matching(html: str) -> bool:
    return 'Pago de Tarjeta de Crédito Otros Bancos' in html


@banorte_email_scraper
def scrape(rows: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([r.strip() for r in [rows[4], rows[18], rows[14]] if r]),
        operation_date=f'{rows[6]} {rows[8]}',
        amount=extract_amount(rows[22]),
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount=extract_amount(rows[26]),
                tax=extract_amount(rows[28]),
            ),
        ],
        receiver=Receiver(
            name=rows[16],
            bank=rows[20],
        ),
    )
