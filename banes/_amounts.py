import re


def extract_amount(raw_amount: str) -> str:
    match = re.search(r'\d+\.\d+', raw_amount.replace(',', ''))[0]  # type: ignore
    number = float(match)

    return f'{number:.2f}'


def extract_amount_spei(raw_amount: str) -> str:
    number = float(raw_amount.replace(',', ''))

    return f'{number:.2f}'
