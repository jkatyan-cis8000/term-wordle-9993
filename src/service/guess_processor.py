"""Parse user input and validate guesses."""

from src.types.guess_result import GuessResult
from src.utils.validation import is_valid_word
from src.repo.word_repository import WordRepository


class GuessProcessor:
    """Processes user guesses and computes feedback."""
    
    def __init__(self):
        self.word_repository = WordRepository()
    
    def get_target_word(self) -> str:
        """Get today's daily word."""
        return self.word_repository.get_daily_word()
    
    def process_guess(self, guessed_word: str, target_word: str) -> GuessResult:
        """Process a guess and return result with feedback."""
        guessed_word = guessed_word.upper()
        target_word = target_word.upper()
        
        correct_positions = []
        partial_matches = []
        invalid_letters = []
        guessed_chars = list(guessed_word)
        target_chars = list(target_word)
        
        for i in range(len(guessed_word)):
            if guessed_chars[i] == target_chars[i]:
                correct_positions.append(i)
                guessed_chars[i] = None
                target_chars[i] = None
        
        for i in range(len(guessed_word)):
            if guessed_chars[i] is not None:
                if guessed_chars[i] in target_chars:
                    partial_matches.append(i)
                    idx = target_chars.index(guessed_chars[i])
                    target_chars[idx] = None
                else:
                    invalid_letters.append(guessed_word[i])
        
        return GuessResult(
            target_word=target_word,
            guessed_word=guessed_word,
            correct_positions=correct_positions,
            partial_matches=partial_matches,
            invalid_letters=invalid_letters
        )
    
    def is_valid_guess(self, guess: str) -> bool:
        """Check if the guess is valid."""
        return is_valid_word(guess)
