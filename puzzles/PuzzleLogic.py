from puzzles.Puzzle import Puzzle


def populate_puzzles():
    puzzle_options = ["Option 1", "Option 2", "Option 3", "Option 4"]
    puzzle = Puzzle("What is the option I am thinking of right now?", puzzle_options, "Option 1", "images/puzzle1.jpg")

    return puzzle