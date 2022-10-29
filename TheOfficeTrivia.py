""""
The following set of code is a program for a multiple choice quiz/trivia. It has six straightforward
questions from the sitcom "The Office". This is a program made for pass-time fun rather than for
achieving a specific task and it is a great solution for curing boredom after finishing the show.You answer
the multiple choice questions and at the end it gives you a final score. It also allows you to play again
if you would like.
"""

# below, I made a dictionary so I can associate my set of questions in the quiz to their corresponding answers
questions = {
 "What is the name of the paper company that they work at in the show?: ": "D",
 "Who is the Scranton regional manager in the beginning of the show?: ": "B",
 "Who is Pam engaged with in the beginning of the show?: ": "C",
 "Where do Jim and Pam get married?: ": "A",
 "What is the name of Angela's cat that Dwight kills?: ": "B",
 "Which character does Micheal hate the most?: ": "C"
}

# below is a list of multiple lists which contain the A,B,C and D options for each question from
# which the user has to answer
options = [["A. Dundie Miffler", "B. Dunder Miffler", "C. Dander Muffin", "D. Dunder Mifflin"],
          ["A. Jim Halpert", "B. Micheal Scott", "C. Dwight Schrute", "D. It was still to be decided"],
          ["A. Jim", "B. Chris", "C. Roy", "D. She is not engaged to anyone"],
          ["A. Niagara Falls", "B. Las Vegas", "C. Schrute Farms", "D. A banquet hall in Scranton"],
          ["A. Princess Lady", "B. Sprinkles", "C. Garbage", "D. Bandit"],
          ["A. Ryan", "B. Kelly", "C. Toby", "D. Creed"]]

def play_game():
    """"
    Displays the questions and options and compares the user's guess to the corresponding key pair for
    that question from the dictionary. If it matches, number of correct guesses increases by 1 which
    is their score.
    """
    print("-------------------------------")
    correct_guesses = 0
    question_num = 1
    # nested for loop below will help display the question before the options
    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter 'A', 'B', 'C' or 'D': ")
        guess = guess.upper()   #in case user decides to put lowercase letters
        correct_guesses += (check_guess(questions[key], guess))
        question_num += 1

    score(correct_guesses)

def check_guess(answer, guess):
    """
    If user guess matches correct answer, a 1 will return so that the 1 point can be added to their score.
    User will also get a short message based on if they answered correct or not to keep the quiz engaging.
    """
    if answer == guess:
        print(" \n THAT IS CORRECT! Well done! \n")
        return 1
    else:
        print(" \n THAT IS INCORRECT! Nice try! \n")
        return 0

def score(correct_guesses):
    """
    Calculation of score by the number of correct guesses by the end of the quiz.
    """
    score = int(((correct_guesses/len(questions))*100))
    print("You got " + str(correct_guesses) + "/" + str(len(questions)) + " correct")
    print("Your score is: "+str(score)+"%")
    print("Great attempt! If you didn't do too well, you have the option to play again. \n")
# provide print of both the fraction and percentage score so users can interpret it in both ways
def play_again():
    """
   Based on user's yes or no answer, they can choose to play again or not. This can be more efficient
   than rerunning the program when the user thinks they want to play again and achieve a better score.
    """
    user_response = input("Would you like to attempt this quiz again? (Give a 'yes' or 'no' answer): ")
    user_response = user_response.lower()
    if user_response == "yes":
        return True
    else:
        return False
# Used boolean data values to consider the entire function to be true or false based on the user's yes
# or no answer so that it is easier to set conditions for whether the quiz should run again or not as shown
# in the code below
play_game()
while play_again():
    play_game()
print("\nThank you for playing!")

# while loop to say in a short and sweet manner that if the function "play_again" was true, it has to
# run the quiz game again