"""ANSI color rendering and board display."""

from src.types.guess_result import GuessResult
from src.utils.color import color_letter


class TerminalDisplay:
    """Handles ANSI color rendering and board display."""
    
    def __init__(self, word_length: int = 5, max_attempts: int = 6):
        self.word_length = word_length
        self.max_attempts = max_attempts
        self.attempts: list[GuessResult] = []
    
    def display_board(self) -> None:
        """Display the current game board with all attempts."""
        for result in self.attempts:
            self._display_guess(result)
        
        for _ in range(self.max_attempts - len(self.attempts)):
            print(" ".join(["_"] * self.word_length))
    
    def _display_guess(self, result: GuessResult) -> None:
        """Display a single guess with colored letters."""
        colored_letters = []
        for i, letter in enumerate(result.guessed_word):
            if i in result.correct_positions:
                colored_letters.append(color_letter(letter, "correct"))
            elif i in result.partial_matches:
                colored_letters.append(color_letter(letter, "partial"))
            else:
                colored_letters.append(color_letter(letter, "invalid"))
        
        print(" ".join(colored_letters))
    
    def add_attempt(self, result: GuessResult) -> None:
        """Add a guess result to the display."""
        self.attempts.append(result)
    
    def display_game_over(self, result: GuessResult) -> None:
        """Display game over message with the target word."""
        print("\n" + "=" * (self.word_length * 2 - 1))
        if result.correct_positions == list(range(self.word_length)):
            print("You won! 🎉")
        else:
            print("Game over!")
        print(f"Target word: {result.target_word}")
        print("=" * (self.word_length * 2 - 1))
    
    def clear_screen(self) -> None:
        """Clear the terminal screen."""
        print("\033[2J\033[H", end="")
