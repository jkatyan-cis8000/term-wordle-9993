"""ANSI color helper functions."""

# ANSI color codes (must match config/settings.py)
_COLOR_GREEN: str = "\033[92m"
_COLOR_YELLOW: str = "\033[93m"
_COLOR_GREY: str = "\033[90m"
_COLOR_RESET: str = "\033[0m"


def color_green(text: str) -> str:
    """Return text with green color."""
    return f"{_COLOR_GREEN}{text}{_COLOR_RESET}"


def color_yellow(text: str) -> str:
    """Return text with yellow color."""
    return f"{_COLOR_YELLOW}{text}{_COLOR_RESET}"


def color_grey(text: str) -> str:
    """Return text with grey color."""
    return f"{_COLOR_GREY}{text}{_COLOR_RESET}"


def color_letter(letter: str, status: str) -> str:
    """Color a letter based on its status."""
    if status == "correct":
        return color_green(letter)
    elif status == "partial":
        return color_yellow(letter)
    else:
        return color_grey(letter)
