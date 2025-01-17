from model.puzzles.Puzzle import Puzzle


# TODO move this logic to a database or a file
def populate_puzzles():
    puzzle_options = ["2", "10", "5", "13"]
    puzzle = Puzzle(
        "What is the output of the following piece of code?",
        """def mystery_function(x):
                return x * 2 if x > 10 else x + 5
                result = mystery_function(8)
                print(result)""",
        puzzle_options,
        "13",
        "images/puzzle1.jpg",
        400,
        """The correct answer is 13 because the function uses a ternary operator that checks if x > 10. Since 8 > 10 is False, the else part executes, returning x + 5. Substituting x = 8, the calculation becomes 8 + 5, which equals 13."""
    )

    return puzzle
