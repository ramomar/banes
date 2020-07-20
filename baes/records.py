from typing import List, Optional, Union
from dataclasses import dataclass, field

EXPENSE_RECORD_TYPE = 'EXPENSE'
ACCOUNT_OPERATION_TYPE = 'ACCOUNT_OPERATION'


@dataclass
class ExtraAmount:
    name: str
    amount: str
    tax: str


@dataclass
class ChannelDetails:
    name: Optional[str] = None
    location: Optional[str] = None


@dataclass
class Channel:
    type: str
    details: Optional[ChannelDetails] = None


@dataclass
class Receiver:
    name: Optional[str]
    bank: Optional[str]


@dataclass
class ExpenseRecord:
    source: str
    type: str
    note: str
    operation_date: Optional[str] = None
    application_date: Optional[str] = None
    receiver: Optional[Receiver] = None
    amount: Optional[str] = None
    channel: Optional[Channel] = None
    extra_amounts: List[ExtraAmount] = field(default_factory=lambda: [])


@dataclass
class AccountOperationRecord:
    source: str
    type: str
    note: str
    operation_date: Optional[str] = None


Record = Union[ExpenseRecord, AccountOperationRecord]
