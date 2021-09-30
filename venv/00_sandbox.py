# functions go here
from time import *
import threading
import random

def yes_no(question):
    valid = False
    while not valid:
        response = input("Have you played "
                         "the game before?").lower()


        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If input no, display instructions
        elif response == "no" or response == "n":
            response = "no"
            return response

        #If input not yes or no, clarify question
        else:
            print("<error> please insert a yes / no")


def want_instructions(question):
    valid = False
    while not valid:
        response = input("Do you want to see the instructions?").lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If input no, display instructions
        elif response == "no" or response == "n":
            response = "no"
            return response

        #If input not yes or no, clarify question
        else:
            print("<error> please insert a yes / no")


def instructions_and_rules():
    print("These are the instructions to the game:")
    print()
    print("You will have 60 seconds to answer as many questions as you can")
    print("When a question is displayed, three options will be provided")
    print("You must type the answer you are wanting to submit, not the letter assigned to it")
    print()
    print("At the beginning of the game you will have three lives")
    print("If you get an answer correct you will get 10 points, and move on to the next question")
    print("If you get an answer wrong it will move on to the next question.")
    print("However you will only get 5 points and 1 life will be deducted.")
    print()
    print("One of three endgame situations will print the following:")
    print("Total Score")
    print("Amount of questions answered correctly")
    print()
    print("The endgame situations being:")
    print("You lose if the timer reaches 0 and you have not answered all the questions.")
    print("You lose if you have 0 lives.")
    print("You win if you answer all the questions with 1 or more lives remaining")
    print()
    print("May be subject to a randomized question quiz - who knows?¯\_(ツ)_/¯")
    print("(Update) I made it randomized >:D")


def countdown():
    global my_timer

    my_timer = 10

    for x in range(10):
        my_timer = my_timer - 1
        sleep(1)

    print()


def statement_generator(statement, decoration):

    sides = decoration * 3

    greeting = "{} {} {}".format(sides, statement, sides)

    top_bottom = decoration * len(greeting)

    print(top_bottom)
    print(greeting)
    print(top_bottom)

    return ""


# main program goes here
test_list = [["What is the most used streaming service?", "netflix", "disney+", "hulu"],
             ["What is the smallest planet in our solar system?", "mercury", "venus", "earth"],
             ["In which country did Lego originate from?", "denmark", "germany", "england"],
             ["What chases the player's character in Pacman?", "ghosts", "goblins", "inner demons and self doubt"]]

correct_answers = ["netflix", "mercury", "denmark", "ghosts"]

question = 1
score = 0
lives = 3
questions_answered = 0

# welcome the user to the game, ask them if they have played before
print("Welcome to the Timer Quiz Game :]")
played_before = yes_no("Have you played before?")
print()

# if they say no, ask them if they want to see the instructions
if played_before == "no":
    instructions = want_instructions("Do you want to see the instructions?")
    if instructions == "no":
        print()
    elif instructions == "yes":
        instructions_and_rules()
    else:
        print()
else:
    print()
play_game = input("Press <Enter> to play")
print()
print("=====================================")

random.shuffle(test_list)
countdown_thread = threading.Thread(target = countdown)
countdown_thread.start()

while my_timer > 0 and play_game == "" and len(test_list) != 0:
    print("Question {}".format(question))
    print(test_list[0][0])
    print("A. {}".format(test_list[0][1]))
    print("B. {}".format(test_list[0][2]))
    print("C. {}".format(test_list[0][3]))
    guess = input("What is your answer?")
    if guess in correct_answers:
        print("CORRECT!")
        score += 10
        questions_answered + 1
    else:
        print("INCORRECT!")
        lives -= 1
        score += 5
    del test_list[0]
    question += 1
    print()

if lives == 0:
    play_game = False
    print("All Lives Lost. Game Over")
    print("You answered {} questions correctly!".format(questions_answered))
    print("Your final score is: {}".format(score))

elif my_timer == 0:
    print("Time's Up!. Game Over")
    print("You answered {} questions correctly!".format(questions_answered))
    print("Your final score is: {}".format(score))

else:
    print("Game Over")
    print("You answered {} questions correctly!".format(questions_answered))
    print("Your final score is: {}".format(score))


