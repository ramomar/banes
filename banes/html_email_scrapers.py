from typing import Callable, List
from bs4 import BeautifulSoup
from .records import Record

HtmlToRecordCallable = Callable[[str], Record]
HtmlRowsToRecordCallable = Callable[[List[str]], Record]


def banorte_email_scraper(scrape: HtmlRowsToRecordCallable) -> HtmlToRecordCallable:
    def _banorte_email_scraper(html: str) -> Record:
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find_all('td')
        sanitized_rows = [row.get_text().strip() for row in rows]

        return scrape(sanitized_rows)

    return _banorte_email_scraper


def banorte_spei_email_scraper(scrape: HtmlRowsToRecordCallable) -> HtmlToRecordCallable:
    def _banorte_spei_email_scraper(html: str) -> Record:
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find_all('p')
        sanitized_rows = [row.get_text().strip() for row in rows]

        return scrape(sanitized_rows)

    return _banorte_spei_email_scraper
