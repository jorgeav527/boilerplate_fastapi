from datetime import datetime

from sqlmodel import Field, SQLModel


class PostModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    user_id: int
    created: datetime
    updated: datetime
