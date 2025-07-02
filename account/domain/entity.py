from dataclasses import dataclass, field
from datetime import datetime, date

@dataclass
class Account:
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    year_of_birth: date
    is_active: bool = True
    updated_at: datetime = field(default_factory=datetime.now)
    created_at: datetime = field(default_factory=datetime.now)

    