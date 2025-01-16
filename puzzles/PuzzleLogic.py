from puzzles.Puzzle import Puzzle


def populate_puzzles():
    puzzle_options = ["Option 1", "Option 2", "Option 3", "Option 4"]
    puzzle = Puzzle(
        "What is the output of the following piece of code?",
        """def mystery_function(x):
                return x * 2 if x > 10 else x + 5
                result = mystery_function(8)
                print(result)""",
        puzzle_options,
        "Option 1",
        "images/puzzle1.jpg",
    )

    return puzzle
