import random
question = random.randint(0, 3)
if question == 1:
    question = "Exagguration in a sentence to provide more emphasis"
elif question == 2:
    question = "Compares one thing to another, normally using like or as"

else:
    question = "Gives human qualities to non-human things"

valid = True
while valid == True:
    answer = input("What language feature is this definition? {}".format(question))
    if answer != "simile":
        print("try again")

