# Get all the data from data.py to main.py but in the form of list of question object from question_model.py
from question_model import Question
from data import question_data,question_data_2,Animal_question_data
from quiz_brain import QuizBrain

question_bank = []

#simpler way
# for question in question_data:
#     question_text = question_data["text"]
#     question_answer = question_data["answer"]
#     new_q = Question(question_text,question_answer)
#     question_bank.append(new_q)

# Ask the user how many questions they want to play?
ask = int(input("For how much question do you want to play? (10/12/60): "))
if ask == 10:
    for i in range(len(Animal_question_data["results"])):
        new_q = Question(Animal_question_data["results"][i]["question"],Animal_question_data["results"][i]["correct_answer"])
        question_bank.append(new_q)
elif ask == 12:
    for i in range(len(question_data)):
        new_q = Question(question_data[i]["text"],question_data[i]["answer"])
        question_bank.append(new_q)
else:
    for i in range(len(question_data_2)):
        new_q = Question(question_data_2[i]["text"],question_data_2[i]["answer"])
        question_bank.append(new_q)

# print(question_bank[1].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your score is {quiz.user_score}/{len(question_bank)}")

