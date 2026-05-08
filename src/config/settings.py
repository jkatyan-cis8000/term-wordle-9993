"""Game constants and configuration."""

from dataclasses import dataclass

# Game constants
WORD_LENGTH: int = 5
MAX_ATTEMPTS: int = 6

# ANSI color codes
COLOR_GREEN: str = "\033[92m"
COLOR_YELLOW: str = "\033[93m"
COLOR_GREY: str = "\033[90m"
COLOR_RESET: str = "\033[0m"


@dataclass
class GameSettings:
    """Game configuration settings."""
    word_length: int = WORD_LENGTH
    max_attempts: int = MAX_ATTEMPTS
    color_green: str = COLOR_GREEN
    color_yellow: str = COLOR_YELLOW
    color_grey: str = COLOR_GREY
    color_reset: str = COLOR_RESET
