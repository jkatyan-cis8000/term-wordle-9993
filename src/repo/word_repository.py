import random
from datetime import datetime

from src.types.word_source import WordSource


class WordRepository(WordSource):
    def __init__(self, word_list_path: str = "src/config/word_list.txt"):
        self.word_list_path = word_list_path
        self._words: list[str] | None = None

    def _load_words(self) -> list[str]:
        if self._words is None:
            with open(self.word_list_path, "r") as f:
                self._words = [line.strip() for line in f if line.strip()]
        return self._words

    def get_daily_word(self) -> str:
        words = self._load_words()
        seed = datetime.now().toordinal()
        random.seed(seed)
        return random.choice(words)
