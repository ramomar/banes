from typing import List
import re
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'EMAIL_UPDATE_SUCCESS_EMAIL'


def is_matching(html: str) -> bool:
    return 'la actualizacion de su\n correo electronico ha finalizado con exito' in html \
           or 'la actualizacion de su correo electronico ha finalizado con exito' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=fields[2].split('.')[0].replace('\n', ''),
        operation_date=re.sub(r'\s+', ' ', fields[4]),
    )
