from abc import abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import TypedDict
from uuid import uuid4


class Metadata(TypedDict):
    pass


@dataclass(frozen=True)
class Event:
    id: str = field(init=False, default_factory=lambda: str(uuid4()))
    created_at: str = field(init=False, default_factory=lambda: datetime.now().isoformat())
    metadata: Metadata = field(init=False, default_factory=lambda: Metadata())

    @classmethod
    def fqn(cls) -> str:
        return f"{cls.__module__}.{cls.__name__}"
