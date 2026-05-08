"""Orchestrate game flow and state management."""

from src.types.game_state import GameState
from src.types.guess_result import GuessResult
from src.service.guess_processor import GuessProcessor
from src.ui.terminal_display import TerminalDisplay
from src.ui.input_handler import InputHandler


class GameLoop:
    """Orchestrates game flow and state management."""
    
    def __init__(
        self,
        guess_processor: GuessProcessor | None = None,
        display: TerminalDisplay | None = None,
        input_handler: InputHandler | None = None
    ):
        self.guess_processor = guess_processor or GuessProcessor()
        self.display = display or TerminalDisplay()
        self.input_handler = input_handler or InputHandler()
        self.game_state = GameState.PLAYING
        self.target_word = self.guess_processor.get_target_word()
        self.attempts_used = 0
    
    def run(self) -> None:
        """Run the main game loop."""
        while self.game_state == GameState.PLAYING:
            self.display.clear_screen()
            self.display.display_board()
            
            guess = self.input_handler.get_guess()
            
            result = self.guess_processor.process_guess(guess, self.target_word)
            self.display.add_attempt(result)
            self.attempts_used += 1
            
            if result.correct_positions == list(range(len(self.target_word))):
                self.game_state = GameState.WON
            elif self.attempts_used >= self.display.max_attempts:
                self.game_state = GameState.LOST
        
        self.display.clear_screen()
        self.display.display_board()
        
        final_result = GuessResult(
            target_word=self.target_word,
            guessed_word=self.target_word,
            correct_positions=list(range(len(self.target_word))) if self.game_state == GameState.WON else [],
            partial_matches=[],
            invalid_letters=[]
        )
        self.display.display_game_over(final_result)
    
    def reset(self) -> None:
        """Reset the game state for a new round."""
        self.game_state = GameState.PLAYING
        self.target_word = self.guess_processor.get_target_word()
        self.attempts_used = 0
        self.display.attempts = []
