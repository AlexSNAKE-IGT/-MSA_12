from dataclasses import dataclass
from pydantic import BaseModel


class CreateBook(BaseModel):
    name: str
    author: str


@dataclass
class Book:
    id: int
    name: str
    author: str
