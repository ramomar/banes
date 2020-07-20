from typing import List
from .records import ExpenseRecord, ExtraAmount, Receiver, EXPENSE_RECORD_TYPE
from .html_email_scrapers import banorte_email_scraper
from .amounts import extract_amount

EMAIL_TYPE = 'FAST_TRANSFER_EMAIL'


def _scrape_fast_transfer_banorte_email(rows: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([r.strip() for r in [rows[4], rows[28], rows[20]] if r]),
        operation_date=f'{rows[6]} {rows[8]}',
        amount=extract_amount(rows[24]),
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount=extract_amount(rows[30]),
                tax=extract_amount(rows[32])
            ),
        ],
        receiver=Receiver(
            bank=rows[22],
            name=rows[16],
        ),
    )


def _scrape_fast_transfer_other_banks_email(rows: List[str]) -> ExpenseRecord:
    return ExpenseRecord(
        type=EXPENSE_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([r.strip() for r in [rows[4], rows[32], rows[24]] if r]),
        operation_date=f'{rows[6]} {rows[8]}',
        amount=extract_amount(rows[28]),
        extra_amounts=[
            ExtraAmount(
                name='fee',
                amount=extract_amount(rows[34]),
                tax=extract_amount(rows[36])
            ),
        ],
        receiver=Receiver(
            bank=rows[26],
            name=rows[20],
        ),
    )


def is_matching(html: str) -> bool:
    return 'Transferencias Rápidas' in html


@banorte_email_scraper
def scrape(rows: List[str]) -> ExpenseRecord:
    bank_index = [i for i, row in enumerate(rows) if 'Banco Destino' in row][0] + 1
    bank = rows[bank_index]

    if 'Banorte' in bank:
        return _scrape_fast_transfer_banorte_email(rows)
    else:
        return _scrape_fast_transfer_other_banks_email(rows)
