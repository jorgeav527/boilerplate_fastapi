from dataclasses import dataclass
from datetime import datetime


@dataclass
class Post:
    id: int | None
    title: str
    content: str
    user_id: int
    created: datetime
    updated: datetime
