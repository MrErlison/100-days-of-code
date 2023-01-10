"""
The code provided defines a simple true or false quiz 
game. The game consists of two classes, Question and 
QuizBrain, and a single function play_game().

The Question class has two attributes, text and answer, 
and a __init__ method which sets these values when a new 
Question object is created.

The QuizBrain class has three attributes, question_number, 
score, and question_list. The question_number attribute 
keeps track of which question the game is currently on, 
the score attribute keeps track of how many questions the 
user has answered correctly, and the question_list 
attribute is a list of Question
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def play_game():
    """ 
    Play the game by initializing the question bank, creating the quiz and asking questions. 
    """
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")

if __name__ == "__main__":
    play_game()
