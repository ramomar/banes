from typing import List
from .records import AccountOperationRecord, ACCOUNT_OPERATION_TYPE
from ._html_email_scrapers import banorte_email_scraper
from ._format import remove_extra_whitespaces

EMAIL_TYPE = 'EMAIL_UPDATE_SUCCESS_EMAIL'


def is_matching(html: str) -> bool:
    return 'Le notificamos que la actualizacion de su\n correo electronico ha finalizado con exito' in html or\
           'Le notificamos que la actualizacion de su\r\n correo electronico ha finalizado con exito' in html or\
           'Le notificamos que la actualizacion de su correo electronico ha finalizado con exito' in html


@banorte_email_scraper
def scrape(fields: List[str]) -> AccountOperationRecord:
    return AccountOperationRecord(
        type=ACCOUNT_OPERATION_TYPE,
        source=EMAIL_TYPE,
        note=fields[2].split('.')[0].replace('\n', ''),
        operation_date=remove_extra_whitespaces(fields[4]),
    )
