class Puzzle:
    def __init__(
        self, question_title, question, options, correct_answer, image_path, rating
    ):
        self.question_title = question_title
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.image_path = image_path
        self.rating = rating

    def check_answer(self, answer):
        return answer == self.correct_answer

    def get_correct_answer(self):
        return self.correct_answer

    def get_image_path(self):
        return self.image_path

    def get_rating(self):
        return self.rating
