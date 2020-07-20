import pytest
from baes import banorte_email


def test_scrape_account_info_email(load_email):
    """it should be able to identify and scrape data from an account info email"""
    html = load_email('account-info-email.html')
    actual = banorte_email.scrape(html).source
    expected = 'ACCOUNT_INFO_EMAIL'

    assert actual == expected


def test_scrape_cash_withdrawal_email(load_email):
    """it should be able to identify and scrape data from a cash withdrawal email"""
    html = load_email('cash-withdrawal-email.html')
    actual = banorte_email.scrape(html).source
    expected = 'CASH_WITHDRAWAL_EMAIL'

    assert actual == expected


def test_scrape_cash_withdrawal_alt_email(load_email):
    """it should be able to identify and scrape data from cash withdrawal alt email"""
    html = load_email('cash-withdrawal-alt-email.html')
    actual = banorte_email.scrape(html).source
    expected = 'CASH_WITHDRAWAL_ALT_EMAIL'

    assert actual == expected


def test_scrape_charge_email(load_email):
    """it should be able to identify and scrape data from a charge email"""
    html = load_email('charge-email.html')
    actual = banorte_email.scrape(html).source
    expected = 'CHARGE_EMAIL'

    assert actual == expected


def test_cc_payment_other_banks_email(load_email):
    """it should be able to identify and scrape data from a credit card payment other banks email"""
    html = load_email('credit-card-payment-other-banks-email.html')
    actual = banorte_email.scrape(html).source
    expected = 'CREDIT_CARD_PAYMENT_OTHER_BANKS_EMAIL'

    assert actual == expected


def test_debit_card_blocked_email(load_email):
    """it should be able to identify and scrape data from a debit card blocked email"""
    html = load_email('debit-card-blocked-email.html')
    actual = banorte_email.scrape(html).source
    expected = 'DEBIT_CARD_BLOCKED_EMAIL'

    assert actual == expected


def test_deposit_email(load_email):
    """it should be able to identify and scrape data from a deposit email"""
    html = load_email('deposit-email.html')
    actual = banorte_email.scrape(html).source
    expected = 'DEPOSIT_EMAIL'

    assert actual == expected


def test_ddc_activated_email(load_email):
    """it should be able to identify and scrape data from a digital debit card activated email"""
    html = load_email('digital-debit-card-activated-email.html')
    actual = banorte_email.scrape(html).source
    expected = 'DIGITAL_DEBIT_CARD_ACTIVATED_EMAIL'

    assert actual == expected


def test_ddc_blocked_email(load_email):
    """it should be able to identify and scrape data from a digital debit card activated email"""
    html = load_email('digital-debit-card-blocked-email.html')
    actual = banorte_email.scrape(html).source
    expected = 'DIGITAL_DEBIT_CARD_BLOCKED_EMAIL'

    assert actual == expected


def test_ddc_canceled_email(load_email):
    """it should be able to identify and scrape data from a digital debit card canceled email"""
    html = load_email('digital-debit-card-canceled-email.html')
    actual = banorte_email.scrape(html).source
    expected = 'DIGITAL_DEBIT_CARD_CANCELED_EMAIL'

    assert actual == expected


def test_scrape_fast_transfer_banorte_email(load_email):
    """it should be able to identify and scrape data from a fast transfer email (banorte)"""
    html = load_email('fast-transfer-banorte-email.html')
    actual = banorte_email.scrape(html).source
    expected = 'FAST_TRANSFER_EMAIL'

    assert actual == expected


def test_scrape_fast_transfer_other_banks_email(load_email):
    """it should be able to identify and scrape data from a fast transfer email (other banks)"""
    html = load_email('fast-transfer-other-banks-email.html')
    actual = banorte_email.scrape(html).source
    expected = 'FAST_TRANSFER_EMAIL'

    assert actual == expected


def test_multiple_matches_exception():
    """it should throw if there are multiple matches"""
    pass


def test_scraper_not_implemented_exception():
    """it should throw when a scraper has not been implemented"""
    with pytest.raises(banorte_email.ScraperNotImplementedException) as excinfo:
        banorte_email.scrape('<a></a>')

        assert 'Scraper not implemented' in excinfo.value
