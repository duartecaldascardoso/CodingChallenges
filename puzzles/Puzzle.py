class Puzzle:
    # Puzzle class that has a list with 4 options, the correct answer, and the question
    def __init__(self, question_title, question, options, correct_answer, image_path):
        self.question_title = question_title
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.image_path = image_path

    # Method that prints the question and the options
    def print_question(self):
        print(self.question_title)
        print(self.question)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

    # Method that checks if the answer is correct
    def check_answer(self, answer):
        return answer == self.correct_answer

    # Method that returns the correct answer
    def get_correct_answer(self):
        return self.correct_answer

    # Method that returns the image path
    def get_image_path(self):
        return self.image_path
