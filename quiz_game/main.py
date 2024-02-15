from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_comment = question["comment"]
    new_question = Question(text=question_text, answer=question_answer, comment=question_comment)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've reached the end of the quiz!")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")
