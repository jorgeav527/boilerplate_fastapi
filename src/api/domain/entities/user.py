from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: str | None
    name: str
    created: datetime
    updated: datetime | None
