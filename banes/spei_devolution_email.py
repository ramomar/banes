from typing import List
from .records import IncomeRecord, INCOME_RECORD_TYPE
from ._html_email_scrapers import banorte_spei_email_scraper
from ._amounts import extract_amount_spei
from ._format import remove_extra_whitespaces

EMAIL_TYPE = 'SPEI_DEVOLUTION_EMAIL'


def is_matching(html: str) -> bool:
    return 'SPEI' in html and ('Devolucion' in html or 'Extemporanea' in html)


@banorte_spei_email_scraper
def scrape(fields: List[str]) -> IncomeRecord:
    note = ' '.join(fields[7:10]).rstrip()
    sanitized_note = remove_extra_whitespaces(note)

    operation_data = sanitized_note.split(' ')

    return IncomeRecord(
        type=INCOME_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=sanitized_note,
        operation_date=f'{operation_data[12]} {operation_data[15]}',
        amount=extract_amount_spei(operation_data[9]),
    )
