# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint.

## Module Structure

### Types Layer (`src/types/`)
- `__init__.py`: Type exports
- `game_state.py`: GameState enum (PLAYING, WON, LOST)
- `guess_result.py`: GuessResult dataclass (correct positions, partial matches, invalid letters)
- `word_source.py`: WordSource protocol (daily word retrieval)

### Config Layer (`src/config/`)
- `__init__.py`: Config exports
- `settings.py`: Game constants (WORD_LENGTH=5, MAX_ATTEMPTS=6, ANSI codes)
- `word_list.py`: Daily word list (2000+ common 5-letter English words)

### Repo Layer (`src/repo/`)
- `__init__.py`: Repo exports
- `word_repository.py`: Loads word list from file, selects daily word

### Service Layer (`src/service/`)
- `__init__.py`: Service exports
- `game_engine.py`: Core game logic - validate guesses, compute feedback
- `guess_processor.py`: Parse user input, validate word, compute result

### Runtime Layer (`src/runtime/`)
- `__init__.py`: Runtime exports
- `game_loop.py`: Orchestrates the game flow, manages state

### UI Layer (`src/ui/`)
- `__init__.py`: UI exports
- `terminal_display.py`: ANSI color rendering, board display
- `input_handler.py`: Terminal input parsing, user prompts

### Utils Layer (`src/utils/`)
- `__init__.py`: Utils exports
- `color.py`: ANSI color helper functions
- `validation.py`: Pure validation helpers (is_alpha, is_length)

## Interfaces

### Service Layer Exposes:
- `GameEngine`: `submit_guess(guess: str) -> GuessResult | None` - processes guess, returns result or None if invalid
- `GuessProcessor`: `process(raw_input: str) -> tuple[bool, str]` - validates and normalizes input

### Repo Layer Exposes:
- `WordRepository`: `get_daily_word() -> str` - returns current day's 5-letter word

### UI Layer Exposes:
- `TerminalDisplay`: `show_board(guesses: list[GuessResult], attempts: int)` - renders game board
- `TerminalDisplay`: `show_result(game_state: GameState, word: str)` - shows win/loss message
- `InputHandler`: `get_guess(attempt: int) -> str` - prompts user for guess

## Shared Data Structures

### GuessResult (dataclass)
```python
@dataclass
class GuessResult:
    target_word: str
    guessed_word: str
    correct_positions: list[int]  # indices where letter matches position
    partial_matches: list[int]    # indices where letter exists but wrong position
    invalid_letters: list[str]    # letters not in word
```

### GameState (enum)
```python
class GameState(Enum):
    PLAYING = "playing"
    WON = "won"
    LOST = "lost"
```

## External Dependencies

- **Python stdlib only**: No external packages required
  - `dataclasses`: Data structure definitions
  - `enum`: GameState enum
  - `random`: Daily word selection
  - `datetime`: Daily cycle determinism
