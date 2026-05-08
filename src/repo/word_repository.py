"""Word loading and daily word selection."""

import random
from datetime import datetime

from src.config.word_list import DAILY_WORD_LIST


class WordRepository:
    """Loads word list and selects the daily word deterministically."""
    
    def get_daily_word(self) -> str:
        """Return today's word based on date."""
        today = datetime.now().date()
        seed_value = today.toordinal()
        random.seed(seed_value)
        return random.choice(DAILY_WORD_LIST)
