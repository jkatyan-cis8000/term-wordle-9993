"""ANSI color helper functions."""

from src.config.settings import (
    COLOR_GREEN,
    COLOR_YELLOW,
    COLOR_GREY,
    COLOR_RESET
)


def color_green(text: str) -> str:
    """Return text with green color."""
    return f"{COLOR_GREEN}{text}{COLOR_RESET}"


def color_yellow(text: str) -> str:
    """Return text with yellow color."""
    return f"{COLOR_YELLOW}{text}{COLOR_RESET}"


def color_grey(text: str) -> str:
    """Return text with grey color."""
    return f"{COLOR_GREY}{text}{COLOR_RESET}"


def color_letter(letter: str, status: str) -> str:
    """Color a letter based on its status."""
    if status == "correct":
        return color_green(letter)
    elif status == "partial":
        return color_yellow(letter)
    else:
        return color_grey(letter)
