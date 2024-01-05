from question import Question
from data import question_data
from quiz_game import Quiz_Game

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz_Game(question_bank)

wrong_ans = False

while quiz.still_has_questions():
    quiz.next_question()        

quiz.end_of_quiz()
