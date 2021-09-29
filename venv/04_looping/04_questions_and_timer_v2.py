from time import *
import threading

def countdown():
    global my_timer

    my_timer = 10

    for x in range(10):
        my_timer = my_timer - 1
        sleep(1)

    print()

countdown_thread = threading.Thread(target = countdown)

countdown_thread.start()

test_list = [["What is the most used streaming service?", "netflix", "disney+", "hulu"],
             ["What is the smallest planet in our solar system?", "mercury", "venus", "earth"],
             ["In which country did Lego originate from?", "denmark", "germany", "england"]]

correct_answers = ["netflix", "mercury", "denmark"]

question = 1

while my_timer > 0:
    print("Question {}".format(question))
    print(test_list[0][0])
    sleep(0.5)
    print("A. {}".format(test_list[0][1]))
    sleep(0.5)
    print("B. {}".format(test_list[0][2]))
    sleep(0.5)
    print("C. {}".format(test_list[0][3]))
    sleep(0.5)
    guess = input("What is your answer?")
    if guess in correct_answers:
        print("CORRECT!")
    else:
        print("INCORRECT")
    del test_list[0]
    question += 1
    print()

print()
print("Time's Up!")
