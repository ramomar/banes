from typing import Dict, List, Tuple, Callable, Optional, Any
from .records import Record
from . import account_info_email
from . import cash_withdrawal_email
from . import cash_withdrawal_alt_email
from . import charge_email
from . import cc_payment_other_banks_email
from . import dc_blocked_email
from . import deposit_email
from . import ddc_activated_email
from . import ddc_blocked_email
from . import ddc_canceled_email
from . import fast_transfer_email
from . import id_by_phone_email
from . import limit_modification_email
from . import nip_change_email
from . import phone_recharge_email
from . import service_payment_email
from . import spei_devolution_email
from . import spei_income_email
from . import banorte_movil_activation_email
from . import banorte_movil_cancelation_email
from . import contact_media_update_email
from . import cc_payment_third_parties
from . import email_change_confirmation_email
from . import notification_medium_change_email
from . import email_update_success_email
from . import third_party_account_registration_email
from . import transfer_national_banks_spei_email


class MultipleMatchesException(Exception):
    """Raise when there are multiple matching scrapers"""


class ScraperNotImplementedException(Exception):
    """Raise when the scraper has not been implemented"""


# List[Any] so as to avoid some mypy complaints
_email_scrapers: List[Any] = [
    account_info_email,
    cash_withdrawal_email,
    cash_withdrawal_alt_email,
    charge_email,
    cc_payment_other_banks_email,
    dc_blocked_email,
    deposit_email,
    ddc_activated_email,
    ddc_blocked_email,
    ddc_canceled_email,
    fast_transfer_email,
    id_by_phone_email,
    limit_modification_email,
    nip_change_email,
    phone_recharge_email,
    service_payment_email,
    spei_devolution_email,
    spei_income_email,
    banorte_movil_activation_email,
    banorte_movil_cancelation_email,
    contact_media_update_email,
    cc_payment_third_parties,
    email_change_confirmation_email,
    notification_medium_change_email,
    email_update_success_email,
    third_party_account_registration_email,
    transfer_national_banks_spei_email,
]

_email_type_to_scraper: Dict[str, Callable[[str], Record]] =\
    dict([(email_scraper.EMAIL_TYPE, email_scraper.scrape) for email_scraper in _email_scrapers])

_email_type_to_matcher: List[Tuple[str, Callable[[str], bool]]] =\
    [(email_scraper.EMAIL_TYPE, email_scraper.is_matching) for email_scraper in _email_scrapers]


def _get_email_type(html: str) -> Optional[str]:
    matches = [email_type for (email_type, is_matching) in _email_type_to_matcher if is_matching(html)]

    if len(matches) > 1:
        raise MultipleMatchesException(f'Multiple matches: {", ".join(matches)}')

    if len(matches) == 0:
        return None

    return matches[0]


def scrape(html: str) -> Record:
    email_type = _get_email_type(html)

    if email_type:
        scraper = _email_type_to_scraper[email_type]
    else:
        raise ScraperNotImplementedException('Scraper not implemented')

    return scraper(html)
