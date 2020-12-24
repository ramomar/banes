from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper

EMAIL_TYPE = 'EMAIL_CHANGE_CONFIRMATION_EMAIL'


def is_matching(html: str) -> bool:
    return 'Banorte recibió una solicitud para que se asigne este correo a su cuenta' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=fields[1],
    )
