from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    description: str
    state: bool = False
    updated_at: datetime
    created_at: datetime