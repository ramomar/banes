from typing import Dict, List, Tuple, Callable, Optional
from .record import Record
from . import account_info_email
from . import cash_withdrawal_email
from . import cash_withdrawal_alt_email
from . import charge_email
from . import cc_payment_other_banks_email
from . import dc_card_blocked_email
from . import fast_transfer_email


class MultipleMatchesException(Exception):
    """Raise when there are multiple matching scrapers"""


class ScraperNotImplementedException(Exception):
    """Raise when there is no matching scraper"""


_email_scrapers = [
    account_info_email,
    cash_withdrawal_email,
    cash_withdrawal_alt_email,
    charge_email,
    cc_payment_other_banks_email,
    dc_card_blocked_email,
    fast_transfer_email,
]

_email_type_to_scraper: Dict[str, Callable[[str], Record]] =\
    dict([(email_scraper.EMAIL_TYPE, email_scraper.scrape) for email_scraper in _email_scrapers])

_email_type_to_matcher: List[Tuple[str, Callable[[str], bool]]] =\
    [(email_scraper.EMAIL_TYPE, email_scraper.is_matching) for email_scraper in _email_scrapers]


def _get_email_type(html: str) -> Optional[str]:
    matches = [email_type for (email_type, is_matching) in _email_type_to_matcher if is_matching(html)]

    if len(matches) > 1:
        raise MultipleMatchesException(f'Multiple matches: {", ".join(matches)}.')

    if len(matches) == 0:
        return None

    return matches[0]


def scrape(html: str) -> Record:
    email_type = _get_email_type(html)

    try:
        scraper = _email_type_to_scraper[email_type]
    except KeyError:
        raise ScraperNotImplementedException('Scraper not implemented')

    return scraper(html)
