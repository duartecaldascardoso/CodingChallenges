"""Challenge class that represents a challenge in the system."""


class Challenge:
    def __init__(
        self,
        name,
        weighted_difficulty,
        category: str,
        puzzle_list: list[str],
        programming_language: str,
    ):
        self.name = name
        self.weighted_difficulty = weighted_difficulty
        self.category = category
        self.puzzle_list = puzzle_list
        self.programming_language = programming_language

    def get_name(self):
        return self.name

    def get_weighted_difficulty(self):
        return self.weighted_difficulty

    def get_category(self):
        return self.category

    def get_puzzle_list(self):
        return self.puzzle_list

    def get_programming_language(self):
        return self.programming_language
