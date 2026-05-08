"""Pure validation helpers."""

# Word length constant (must match config/settings.py)
_WORD_LENGTH: int = 5


def is_alpha(word: str) -> bool:
    """Check if word contains only alphabetic characters."""
    return word.isalpha()


def is_length(word: str, length: int = _WORD_LENGTH) -> bool:
    """Check if word has the expected length."""
    return len(word) == length


def is_valid_word(word: str, length: int = _WORD_LENGTH) -> bool:
    """Check if word is valid (alphabetic and correct length)."""
    return is_alpha(word) and is_length(word, length)
