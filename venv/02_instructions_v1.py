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
    print("=====================================")


# main program goes here
print("Welcome to the Timer Quiz Game :]")
played_before = yes_no("Have you played before?")
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
while play_game == "":
    print()
