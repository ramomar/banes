from typing import List, Optional, Union
from dataclasses import dataclass, field

EXPENSE_RECORD_TYPE = 'EXPENSE'
ACCOUNT_OPERATION_TYPE = 'ACCOUNT_OPERATION'
INCOME_RECORD_TYPE = 'INCOME'


@dataclass(frozen=True)
class ExtraAmount:
    name: str
    amount: str
    tax: str


@dataclass(frozen=True)
class ChannelDetails:
    name: Optional[str] = None
    location: Optional[str] = None


@dataclass(frozen=True)
class Channel:
    type: str
    details: Optional[ChannelDetails] = None


@dataclass(frozen=True)
class Receiver:
    name: Optional[str]
    bank: Optional[str]


@dataclass(frozen=True)
class ExpenseRecord:
    source: str
    type: str
    note: str
    amount: str
    operation_date: Optional[str] = None
    application_date: Optional[str] = None
    receiver: Optional[Receiver] = None
    channel: Optional[Channel] = None
    extra_amounts: List[ExtraAmount] = field(default_factory=lambda: [])


@dataclass(frozen=True)
class AccountOperationRecord:
    source: str
    type: str
    note: str
    operation_date: Optional[str] = None
    channel: Optional[Channel] = None


@dataclass(frozen=True)
class IncomeRecord:
    source: str
    type: str
    note: str
    amount: str
    operation_date: Optional[str] = None


Record = Union[ExpenseRecord, AccountOperationRecord, IncomeRecord]
