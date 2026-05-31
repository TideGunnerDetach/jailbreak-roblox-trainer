from dataclasses import dataclass

@dataclass
class Config:
    interval: float = 1.0
    auto_arrest: bool = False
    auto_escape: bool = False