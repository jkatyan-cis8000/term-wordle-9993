from typing import Protocol


class WordSource(Protocol):
    def get_daily_word(self) -> str:
        ...
