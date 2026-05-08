"""Pure validation helpers."""

from src.config.settings import WORD_LENGTH


def is_alpha(word: str) -> bool:
    """Check if word contains only alphabetic characters."""
    return word.isalpha()


def is_length(word: str, length: int = WORD_LENGTH) -> bool:
    """Check if word has the expected length."""
    return len(word) == length


def is_valid_word(word: str, length: int = WORD_LENGTH) -> bool:
    """Check if word is valid (alphabetic and correct length)."""
    return is_alpha(word) and is_length(word, length)
