from typing import List
import re
from .records import IncomeRecord, INCOME_RECORD_TYPE
from .html_email_scrapers import banorte_spei_email_scraper
from .amounts import extract_amount_spei

EMAIL_TYPE = 'SPEI_DEVOLUTION_EMAIL'


def is_matching(html: str) -> bool:
    return 'SPEI' in html and ('Devolucion' in html or 'Extemporanea' in html)


@banorte_spei_email_scraper
def scrape(rows: List[str]) -> IncomeRecord:
    note = ' '.join(rows[7:10]).rstrip()
    sanitized_note = re.sub(r'\s+', ' ', note)

    operation_data = sanitized_note.split(' ')

    return IncomeRecord(
        type=INCOME_RECORD_TYPE,
        source=EMAIL_TYPE,
        note=sanitized_note,
        operation_date=f'{operation_data[12]} {operation_data[15]}',
        amount=extract_amount_spei(operation_data[9]),
    )

