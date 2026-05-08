"""Terminal input parsing for guesses."""

from src.utils.validation import is_valid_word
from src.config.settings import WORD_LENGTH


class InputHandler:
    """Handles terminal input parsing for guesses."""
    
    def __init__(self, word_length: int = WORD_LENGTH):
        self.word_length = word_length
    
    def get_guess(self, prompt: str = "Enter your guess: ") -> str:
        """Get a valid guess from the user."""
        while True:
            try:
                user_input = input(prompt).strip().upper()
                
                if not user_input:
                    continue
                
                if not is_valid_word(user_input, self.word_length):
                    print(f"Invalid guess. Enter a {self.word_length}-letter word.")
                    continue
                
                return user_input
            except EOFError:
                print("\nInput stream ended. Exiting...")
                raise SystemExit(0)
    
    def get_yes_no(self, prompt: str = "Play again? (y/n): ") -> bool:
        """Get a yes/no answer from the user."""
        while True:
            try:
                user_input = input(prompt).strip().lower()
                if user_input in ("y", "yes"):
                    return True
                elif user_input in ("n", "no"):
                    return False
                print("Please enter 'y' or 'n'.")
            except EOFError:
                return False
