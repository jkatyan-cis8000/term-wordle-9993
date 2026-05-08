"""Core game logic for processing guesses and managing game state."""

from typing import Optional

from src.repo.word_repository import WordRepository
from src.types.game_state import GameState
from src.types.guess_result import GuessResult
from src.types.word_source import WordSource


class GameEngine:
    """Manages game state and processes user guesses."""

    def __init__(self, word_source: Optional[WordSource] = None):
        """Initialize game with optional custom word source for testing."""
        self.word_source = word_source or WordRepository()
        self.daily_word = self.word_source.get_daily_word()
        self.attempts_remaining = 6
        self.guesses: list[GuessResult] = []
        self.state = GameState.PLAYING

    def submit_guess(self, guess: str) -> GuessResult:
        """Process a guess and return results."""
        if self.state != GameState.PLAYING:
            raise ValueError("Game is not in playing state")

        guess = guess.upper()
        if len(guess) != 5:
            raise ValueError("Guess must be exactly 5 letters")

        result = self._evaluate_guess(guess)
        self.guesses.append(result)
        self._update_state(guess, result)

        return result

    def _evaluate_guess(self, guess: str) -> GuessResult:
        """Evaluate a guess against the daily word."""
        target = self.daily_word.upper()
        correct_positions: list[int] = []
        partial_matches: list[int] = []
        invalid_letters: list[str] = []

        target_list = list(target)
        guess_list = list(guess)

        for i in range(5):
            if guess_list[i] == target_list[i]:
                correct_positions.append(i)
                target_list[i] = None
                guess_list[i] = None

        for i in range(5):
            if guess_list[i] is not None:
                if guess_list[i] in target_list:
                    partial_matches.append(i)
                    target_list[target_list.index(guess_list[i])] = None
                else:
                    invalid_letters.append(guess_list[i])

        return GuessResult(
            target_word=target,
            guessed_word=guess,
            correct_positions=correct_positions,
            partial_matches=partial_matches,
            invalid_letters=invalid_letters,
        )

    def _update_state(self, guess: str, result: GuessResult) -> None:
        """Update game state based on the guess result."""
        if guess == self.daily_word.upper():
            self.state = GameState.WON
            self.attempts_remaining = 0
        elif self.attempts_remaining == 1:
            self.state = GameState.LOST
            self.attempts_remaining = 0
        else:
            self.attempts_remaining -= 1
