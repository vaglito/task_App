from dataclasses import dataclass, field
from datetime import datetime
from account.domain.entity import Account


@dataclass
class Task:
    id: int
    title: str
    user: Account
    is_active: bool = True
    description: str = ""
    state: bool = False
    updated_at: datetime = field(default_factory=datetime.now)
    created_at: datetime = field(default_factory=datetime.now)