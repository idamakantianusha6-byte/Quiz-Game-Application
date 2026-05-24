import json
from backend.quiz_logic import QuizGame

def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

if __name__ == "__main__":
    questions = load_questions()
    quiz = QuizGame(questions)
    quiz.start_quiz()
