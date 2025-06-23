# Asking the questions to the user in loop
# Task1 Create a quiz brain class
class QuizBrain():
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        
    user_score = 0
    
    def next_question(self):
        # first approach
        # user_input = input(f"Q {self.question_number +1}: {self.question_list[self.question_number].text} (True / False) : ")
        
        # easier approach
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True / False) : ")
        self.check_answer(user_answer,current_question.answer)
    
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.user_score +=1
        else:
            print("You got it wrong")
        print(f"the correct answer is {correct_answer}")
        print(f"Your score is {self.user_score}/{self.question_number}")
        print("\n")


# Checking if the answer was correct

# Checking if we are at the end of the quiz
    def still_has_question(self):
        return self.question_number < len(self.question_list)
