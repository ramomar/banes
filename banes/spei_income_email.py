from typing import List
from .records import IncomeRecord, INCOME_RECORD_TYPE
from ._html_email_scrapers import banorte_spei_email_scraper
from ._amounts import extract_amount_spei
from ._format import remove_extra_whitespaces

EMAIL_TYPE = 'SPEI_INCOME_EMAIL'


def is_matching(html: str) -> bool:
    return 'SPEI Recibido' in html


@banorte_spei_email_scraper
def scrape(fields: List[str]) -> IncomeRecord:
    sanitized_note = remove_extra_whitespaces(fields[6].rstrip())
    operation_data = sanitized_note.split(' ')

    return IncomeRecord(
        type=INCOME_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=sanitized_note,
        operation_date=f'{operation_data[10]} {operation_data[13]}',
        amount=extract_amount_spei(operation_data[7]),
    )
