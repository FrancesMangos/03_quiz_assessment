# functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input("Have you played "
                         "the game before?").lower()


        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If input no, ask if user wants to see instructions
        elif response == "no" or response == "n":
            response = "no"
            return response

        #If input not yes or no, clarify question
        else:
            print("<error> please insert a yes / no")

def want_instructions(question):
    valid = False
    while not valid:
        response = input("Do you want to see"
                         " the instructions?").lower()

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

# main program goes here
print("Welcome to the Timer Quiz Game :]")
played_before = yes_no("Have you played before?")
if played_before == "no":
    instructions = want_instructions("Do you want to see the instructions?")
    if instructions == "no":
        print()
    elif instructions == "yes":
        print("display instructions")
    else:
        print()
else:
    print()
play_game = input("Press <Enter> to play")
while play_game == "":
    print()
