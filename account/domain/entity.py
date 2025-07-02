from dataclasses import dataclass, field
from datetime import datetime, date

@dataclass
class Account:
    id: int
    is_active: bool = True
    name: str
    last_name: str
    email: str
    password: str
    year_of_birth: date
    updated_at: datetime = field(default_factory=datetime.now)
    created_at: datetime = field(default_factory=datetime.now)

    