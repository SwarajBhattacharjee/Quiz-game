# Asking the questions to the user in loop
# Task1 Create a quiz brain class
class QuizBrain():
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
    
    def next_question(self):
        # first approach
        # user_input = input(f"Q {self.question_number +1}: {self.question_list[self.question_number].text} (True / False) : ")
        
        # easier approach
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True / False) : ")

# Checking if the answer was correct

# Checking if we are at the end of the quiz
