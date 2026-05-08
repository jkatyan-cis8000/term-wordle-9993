from dataclasses import dataclass


@dataclass
class GuessResult:
    target_word: str
    guessed_word: str
    correct_positions: list[int]
    partial_matches: list[int]
    invalid_letters: list[str]
