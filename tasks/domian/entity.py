from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    description: str
    state: bool
    updated_at: datetime
    created_at: datetime