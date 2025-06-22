# Get all the data from data.py to main.py but in the form of list of question object from question_model.py
from question_model import Question
from data import question_data

question_bank = []

#simpler way
# for question in question_data:
#     question_text = question_data["text"]
#     question_answer = question_data["answer"]
#     new_q = Question(question_text,question_answer)
#     question_bank.append(new_q)

for i in range(len(question_data)-1):
    new_q = Question(question_data[i]["text"],question_data[i]["answer"])
    question_bank.append(new_q)
    
print(question_bank[1].answer)
