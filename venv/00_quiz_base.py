# imports go here

from time import *
import threading
import random

# functions go here


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
        response = input("Do you want to see the instructions and rules?").lower()

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
    statement_generator("These are the instructions to the game:", "-")
    print("You have to try and answer as many questions as you can in 120 seconds (2 minutes).")
    print("When a question is displayed you must provide an answer with the three options provided.")
    print("Answer with the letter assigned to the answer.")
    print()
    print("At the beginning of the game you will have 5 lives.")
    print("If you get an answer correct you will get 10 points and move onto the next question.")
    print("If you get an answer wrong you will get 5 points, lose 1 life and move onto the next question.")
    print()
    print("You lose if you lose all 5 lives, or the timer runs out.")
    print("You win if you get through 32 questions with at least 1 life remaining and with time remaining.")
    print()
    print("At the end of the game these will be displayed:")
    print("Amount of questions answered correctly.")
    print("Total Score.")
    print()
    print("=====================================")


def countdown():
    global my_timer

    my_timer = 120

    for x in range(120):
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

# questions in total: 36
quiz_list = [
             ["What is the smallest planet in our solar system?", "Mercury", "Venus", "Earth", "a", "A"],
             ["In which country did Lego originate from?", "Germany", "Denmark", "England", "b", "B"],
             ["What chases the player's character in the game Pacman?", "Ghosts", "Goblins", "Inner demons and self doubt", "a", "A"],
             ["What is a female giraffe called?", "Giraffe", "Cow", "Doe", "b", "B"],
             ["In what year was Marvel's The Avengers released?", 2010, 2011, 2012, "c", "C"],

             ["Scorpions are in what animal class?", "Insects", "Crustaceans", "Arachnids", "c", "C"],
             ["Which one of these are one of the primary colours of light?", "Green", "Yellow", "Magenta", "a", "A"],
             ["Which of these foods can you cook 'sunny-side-up'?", "Steak", "Egg", "Chicken", "b", "B"],
             ["Which apple type shares its name with a famous Japanese mountain?", "Fuji", "Hotaka", "Haku", "a", "A"],
             ["The last word in this phrase, 'She worked methodically' is an example of which writing technique?", "Verb", "Adverb", "Adjective", "b", "B"],

             ["A leech has how many brains?", 32, 42, 52, "a", "A"],
             ["McDonald's opened its first restaurant in which decade?", "1960s", "1950s", "1940s", "b", "B"],
             ["What does the B stand for in FBI?", "Bureau", "Business", "Bigot", "a", "A"],
             ["A newborn joey's size can be comparable to the size of what?", "A Marble", "A Grape", "A Grain of Rice", "c", "C"],
             ["Australia has how many states?", 4, 5, 6, "c", "C"],

             ["Axolotls do not develop which organ when metamorphosing into a salamander?", "Kidneys", "Colon", "Lungs", "c", "C"],
             ["In MineCraft, a Potion of Slow Falling is brewed with what ingredient?", "Dragon's breath", "Chicken feather", "Phantom membrane", "c", "C"],
             ["D is the roman numeral for which number?", 5000, 50000, 500000, "c", "C"],
             ["Which circus prop is the title for a song in the musical 'The Greatest Showman?", "Ring", "Tightrope", "Cannon", "b", "B"],
             ["When was YouTube created?", 2005, 2006, 2007, "a", "A"],

             ["A basic meringue is made up of egg whites and what?", "Water", "Sugar", "Salt", "b", "B"],
             ["National Pikachu Day is on what day of November?", "25th", "26th", "27th", "b", "B"],
             ["Justin.tv is the parent company of which gaming streaming platform?", "Facebook", "Youtube", "Twitch", "c", "C"],
             ["Jellyfish are what percent of water?", "85%", "90%", "95%", "c", "C"],
             ["How many countries are under the rule of the British Empire?", 12, 14, 16, "b", "B"],

             ["What is the Southern most state of America?", "Florida", "Texas", "Orlando", "a", "A"],
             ["Rebecca Black's hit song, released in February of 2011, was named after which day of the week?", "Monday", "Wednesday", "Friday", "c", "C"],
             ["What is AirCon short for?", "Air Conditioner", "Air Conditioning", "Air Condition", "b", "B"],
             ["What is the first name of President Snow from 'The Hunger Games'?", "Camellias", "Coriolanus", "Christian", "b", "B"],
             ["What is the name of the second book in 'The Maze Runner' series?", "The Scorch Trials", "The Death Cure", "The Fever Code", "a", "A"],
             ["Which Disney princess was created from a different studio?", "Tiana", "Merida", "Meg", "b", "B"],

             ["How many students were in Ms Frizzle's class in the original 'The Magic School Bus'?", 20, 22, 24, "a", "A"],
             ["The study of stars is called what?", "Cosmology", "Astrology", "Astronomy", "c", "C"],
             ["On the cover of the book 'Wonder' by R.J. Palacio, where is the eye placed?", "On the Right", "In the Middle", "On the Left", "c", "C"],
             ["What is the name of the train station in which Hogwarts students go to board the Hogwarts Express?", "Queen's Cross", "King's Cross", "King's Crocks", "b", "B"],
             ["In Greek Mythology, staring at what part of Medusa's body turns you to stone?", "Eyes", "Hair", "Mouth", "a", "B"],

             ["A small, hard deposit that forms in the kidneys that is often painful when passed is called a 'Kidney what?'", "Rock", "Stone", "Pebble", "b", "B"],

]


question = 1
score = 0
lives = 5
questions_answered_correctly = 0

# welcome the user to the game, ask them if they have played before
statement_generator("Welcome to Quiz Blitz!", "*")
print("This will test your knowledge and how much you remember from your weird google searches!!! ;]")
print()
played_before = yes_no("Have you played before?")
print()

# if they say no, ask them if they want to see the instructions
if played_before == "no":
    instructions = want_instructions("Do you want to see the instructions and rules?")
    if instructions == "no":
        print()
        print("=====================================")
    elif instructions == "yes":
        instructions_and_rules()
    else:
        print()
else:
    print("=====================================")

# ask the user to start the game
play_game = input("Press <Enter> to start the quiz")
print()
print("=====================================")

# starts the timer and shuffles the questions list to be different each run
random.shuffle(quiz_list)
countdown_thread = threading.Thread(target = countdown)
countdown_thread.start()

# start the game
while my_timer > 0 and play_game == "" and len(quiz_list) != 0 and lives > 0:
    print("Question {}".format(question))
    print(quiz_list[0][0])
    sleep(0.25)
    print("A. {}".format(quiz_list[0][1]))
    sleep(0.25)
    print("B. {}".format(quiz_list[0][2]))
    sleep(0.25)
    print("C. {}".format(quiz_list[0][3]))
    sleep(0.25)
    guess = input("What is your answer?")

    # if the answer is correct
    if guess == quiz_list[0][4] or guess == quiz_list[0][5]:
        statement_generator("CORRECT!", "-")
        score += 10
        questions_answered_correctly += 1

    # if the answer is incorrect
    else:
        statement_generator("INCORRECT!", "-")
        lives -= 1
        score += 5
    del quiz_list[0]
    question += 1
    print("=====================================")

# if all five lives are lost
if lives == 0:
    print("All Lives Lost. Game Over.")
    print("You answered {} questions correctly!".format(questions_answered_correctly))
    print("Your final score is: {}!".format(score))

# if the timer reaches 0
elif my_timer == 0:
    print("Time's Up! Game Over.")
    print("You answered {} questions correctly!".format(questions_answered_correctly))
    print("Your final score is: {}!".format(score))

# if the user has answered 32 questions CORRECTLY
elif questions_answered_correctly == 32:
    print("Congratulations! You win!")
    print("You answered {} questions correctly!".format(questions_answered_correctly))
    print("Your final score is: {}!".format(score))

# if either of the other situations do not happen
else:
    print("Game Over! You did something wrong, I can tell :D")
    print("You answered {} questions correctly!".format(questions_answered_correctly))
    print("Your final score is: {}!".format(score))
print()
statement_generator("Thank you for playing Quiz Blitz!", "*")
