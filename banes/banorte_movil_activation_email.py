from typing import List
import re
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'BANORTE_MOVIL_ACTIVATION_EMAIL'


def is_matching(html: str) -> bool:
    return 'activación de Banorte Móvil' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    content = fields[2]
    date = re.search(r'\d{2}/\w+/\d{4}', content)
    hour = re.search(r'\d{2}:\d{2}:\d{2}', content)
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note='Activación de Banorte Móvil',
        operation_date=f'{date[0]} {hour[0]}',
    )
