import time

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question, options, correct_answer):
        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        start_time = time.time()
        try:
            answer = int(input("\nEnter your choice (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            return

        elapsed_time = time.time() - start_time
        if elapsed_time > 10:
            print("⏱ Time's up! You took too long.")
            return

        if options[answer - 1] == correct_answer:
            print("✅ Correct!")
            self.score += 1
        else:
            print(f"❌ Wrong! Correct answer: {correct_answer}")

    def start_quiz(self):
        print("🎮 Welcome to the Quiz Game!")
        for q in self.questions:
            self.ask_question(q["question"], q["options"], q["answer"])
        print(f"\n🏆 Final Score: {self.score}/{len(self.questions)}")
