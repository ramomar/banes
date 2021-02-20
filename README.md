# banes

![Build and test](https://github.com/ramomar/banes/workflows/Build%20and%20test/badge.svg)

banes (banorte email scraper) is a library for scraping transaction emails from Banorte.

## Scrapers
The library includes 28 scrapers of different types of emails collected over a two year period.

You can take a look [here](https://github.com/ramomar/banes/tree/master/tests/emails) in order to see which emails have an scraper implemented already.

*The parsing of the dates is up to you due to the weird formats Banorte uses. In my opinion those dates are not very accurate. I recommend taking a look at the timestamp of the email when it arrived in your inbox, and then comparing the two dates in order to see which one is better for your use case.*

## Usage
1. Install the package.
```sh
pip install git+ssh://git@github.com/ramomar/banes.git
```

2. Require the scraper and use it!
```python
import base64
from banes import banorte_email

with open('email-in-b64') as email:
    html = base64.b64decode(email.read())

    print(banorte_email.scrape(html))
```

### Example output

```python
ExpenseRecord(
    source='FAST_TRANSFER_EMAIL',
    type='EXPENSE',
    note='Transferencias Rápidas | Pago de una cosa',
    operation_date='20/Jul/2020 22:14:36 horas',
    receiver=Receiver(
        name='Ana',
        bank='BANAMEX'
    ),
    amount='5.00',
    extra_amounts=[
        ExtraAmount(
            name='fee',
            amount='3.00',
            tax='0.48'
        )
    ]
)
```

You can also independently import the scrapers listed [here](https://github.com/ramomar/banes/blob/master/banes/banorte_email.py#L3-L29).

### Record types

| Record type       | Description |
|-------------------|-------------|
| INCOME            | A record that represents an income. |
| EXPENSE           | A record that represents an expense. |
| ACCOUNT_OPERATION | A record that represents an account operation log (change of NIP, virtual card limit modification, etc). |

You can get more details on the structure of the records [here](https://github.com/ramomar/banes/blob/master/banes/records.py).

## Development

### Testing

In order to run tests you might do `pytest`.

### Type checking

In order to run type checking you might do `mypy banes`.
