from typing import List
from .records import ExpenseRecord, ExtraAmount, Receiver, EXPENSE_RECORD_TYPE
from ._html_email_scrapers import banorte_email_scraper
from ._amounts import extract_amount

EMAIL_TYPE = 'FAST_TRANSFER_EMAIL'


def _scrape_fast_transfer_banorte_email(fields: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([f.strip() for f in [fields[4], fields[28], fields[20]] if f]),
        operation_date=f'{fields[6]} {fields[8]}',
        amount=extract_amount(fields[24]),
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount=extract_amount(fields[30]),
                tax=extract_amount(fields[32])
            ),
        ],
        receiver=Receiver(
            bank=fields[22],
            name=fields[16],
        ),
    )


def _scrape_fast_transfer_other_banks_email(fields: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([f.strip() for f in [fields[4], fields[32], fields[24]] if f]),
        operation_date=f'{fields[6]} {fields[8]}',
        amount=extract_amount(fields[28]),
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount=extract_amount(fields[34]),
                tax=extract_amount(fields[36])
            ),
        ],
        receiver=Receiver(
            bank=fields[26],
            name=fields[20],
        ),
    )


def is_matching(html: str) -> bool:
    return 'Transferencias Rápidas' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> ExpenseRecord:
    bank_index = [i for i, field in enumerate(fields) if 'Banco Destino' in field][0] + 1
    bank = fields[bank_index]

    if 'Banorte' in bank:
        return _scrape_fast_transfer_banorte_email(fields)
    else:
        return _scrape_fast_transfer_other_banks_email(fields)
