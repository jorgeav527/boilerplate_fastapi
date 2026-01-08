from datetime import datetime

from sqlmodel import Field, SQLModel


class UserModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    created: datetime
    updated: datetime
