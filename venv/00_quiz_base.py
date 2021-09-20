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
    print()
    print("You will have two minutes to answer as many questions as you can")
    print("There will be a variety of questions to answer; True/False, Word Answers, Math Equations and General Knowledge Questions")
    print()
    print("If you get an answer wrong it will move onto the next question, every wrong answer will be deducted from your final score")
    print("If you get an answer correct you will get one point")
    print()
    print("Once the time is up your score will be displayed, including:")
    print("Overall Score")
    print("Amount of questions answered correctly")
    print("Amount of questions answered incorrectly")
    print()


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
