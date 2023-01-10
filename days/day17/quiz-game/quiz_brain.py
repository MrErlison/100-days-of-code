class QuizBrain:

    def __init__(self, q_list):
        """ 
        Initialize a new QuizBrain object with a list of questions.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        """ 
        Return whether or not there are still questions to be asked. 
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """ 
        Ask the next question and check the answer. 
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """ 
        Check if the user's answer is correct, update the score and print out a message. 
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
