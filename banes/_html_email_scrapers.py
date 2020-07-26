from typing import Callable, List
from bs4 import BeautifulSoup
from .records import Record

HtmlToRecordCallable = Callable[[str], Record]
FieldsToRecordCallable = Callable[[List[str]], Record]


def banorte_email_scraper(scrape: FieldsToRecordCallable) -> HtmlToRecordCallable:
    def _banorte_email_scraper(html: str) -> Record:
        soup = BeautifulSoup(html, 'html.parser')
        fields = soup.find_all('td')
        sanitized_fields = [field.get_text().strip() for field in fields]

        return scrape(sanitized_fields)

    return _banorte_email_scraper


def banorte_spei_email_scraper(scrape: FieldsToRecordCallable) -> HtmlToRecordCallable:
    def _banorte_spei_email_scraper(html: str) -> Record:
        soup = BeautifulSoup(html, 'html.parser')
        fields = soup.find_all('p')
        sanitized_fields = [field.get_text().strip() for field in fields]

        return scrape(sanitized_fields)

    return _banorte_spei_email_scraper
