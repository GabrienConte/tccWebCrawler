from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class UrlInfo:
    link: str
    status: Optional[int] = None
    origem: Optional[str] = None

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "UrlInfo":
        return UrlInfo(
            link=data["link"],
            status=data.get("status"),
            origem=data.get("origem")
        )