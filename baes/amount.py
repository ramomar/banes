import re


def extract_amount(raw_amount: str) -> str:
    match = re.search(r'\d+\.\d+', raw_amount)[0]
    number = float(match)

    return f'{number:.2f}'
