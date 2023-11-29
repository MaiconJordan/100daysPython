from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for i in question_data:
    question = Question(i['text'], i['answer'])
    question_bank.append(question)   




q = QuizBrain(question_bank)

q.next_question()