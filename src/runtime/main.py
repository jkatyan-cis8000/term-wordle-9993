"""Main entry point, wires all layers together."""

from src.runtime.game_loop import GameLoop
from src.service.guess_processor import GuessProcessor
from src.ui.terminal_display import TerminalDisplay
from src.ui.input_handler import InputHandler


def main() -> None:
    """Main entry point, wires all layers together."""
    game_loop = GameLoop(
        guess_processor=GuessProcessor(),
        display=TerminalDisplay(),
        input_handler=InputHandler()
    )
    
    play_again = True
    while play_again:
        game_loop.run()
        play_again = game_loop.input_handler.get_yes_no("Play again? (y/n): ")
        if play_again:
            game_loop.reset()


if __name__ == "__main__":
    main()
