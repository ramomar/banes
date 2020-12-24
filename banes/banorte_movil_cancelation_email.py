from typing import List
import re
from .records import AccountOperationRecord, Channel, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'BANORTE_MOVIL_CANCELATION_EMAIL'


def is_matching(html: str) -> bool:
    return 'Cancelacion del Servicio Banorte Movil' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    print(fields)
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=f'{fields[14]} | {fields[10]} | {fields[12]}',
        operation_date=re.sub(r'\s+', ' ', f'{fields[6]} {fields[8]}'),
    )
