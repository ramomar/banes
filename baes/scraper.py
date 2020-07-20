from typing import Callable, List
from bs4 import BeautifulSoup
from .records import Record


def banorte_email_scraper(scrape: Callable[[List[str]], Record]) -> Callable[[str], Record]:
    def _banorte_email_scraper(html: str) -> Record:
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find_all('td')
        sanitized_rows = [str(row.string).strip() for row in rows]

        return scrape(sanitized_rows)

    return _banorte_email_scraper
