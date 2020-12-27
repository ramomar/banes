from typing import List
from .records import AccountOperationRecord, Channel, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper
from ._format import remove_extra_whitespaces

EMAIL_TYPE = 'NOTIFICATION_MEDIUM_CHANGE_EMAIL'


def is_matching(html: str) -> bool:
    return 'CAMBIO CORREO ELECTRONICO' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=' | '.join([f.strip() for f in [fields[10], fields[6], fields[8]] if f]),
        operation_date=remove_extra_whitespaces(fields[4]),
        channel=Channel(
            type=fields[12],
        ),
    )
