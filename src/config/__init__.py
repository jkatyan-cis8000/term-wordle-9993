"""Config layer exports."""

from .settings import (
    GameSettings,
    WORD_LENGTH,
    MAX_ATTEMPTS,
    COLOR_GREEN,
    COLOR_YELLOW,
    COLOR_GREY,
    COLOR_RESET
)
from .word_list import DAILY_WORD_LIST

__all__ = [
    "GameSettings",
    "WORD_LENGTH",
    "MAX_ATTEMPTS",
    "COLOR_GREEN",
    "COLOR_YELLOW",
    "COLOR_GREY",
    "COLOR_RESET",
    "DAILY_WORD_LIST"
]
