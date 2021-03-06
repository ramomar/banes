from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper
from ._format import remove_extra_whitespaces

EMAIL_TYPE = 'BANORTE_MOVIL_CANCELATION_EMAIL'


def is_matching(html: str) -> bool:
    return 'Cancelacion del Servicio Banorte Movil' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=f'{fields[14]} | {fields[10]} | {fields[12]}',
        operation_date=remove_extra_whitespaces(f'{fields[6]} {fields[8]}'),
    )
