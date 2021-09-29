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
