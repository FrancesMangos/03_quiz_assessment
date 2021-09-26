from time import *
import threading

def countdown():
    global my_timer

    my_timer = 20

    for x in range(20):
        my_timer = my_timer - 1
        sleep(1)

    print()

countdown_thread = threading.Thread(target = countdown)

countdown_thread.start()

while my_timer > 0:
    print("STAGE ONE: EASY")
    print("Question 1:")
    sleep(1.0)
    print("Which planet is the smallest in our solar system?")
    sleep(1.0)
    print("A. Earth")
    sleep(0.5)
    print("B. Mercury")
    sleep(0.5)
    print("C. Venus")
    sleep(0.5)
    answer = input("Please enter your answer:")
    if answer != "B":
        print("Incorrect!")
    else:
        print("Correct")

    sleep(1.0)
    if my_timer == 0:
        break
    print()

    print("Question 2:")
    sleep(1.0)
    print("Which country has the highest population?")
    sleep(1.0)
    print("A. China")
    sleep(0.5)
    print("B. India")
    sleep(0.5)
    print("C. U.S.A")
    sleep(0.5)
    answer = input("Please enter your answer:")
    if answer != "A":
        print("Incorrect!")
    else:
        print("Correct")

    sleep(1.0)
    if my_timer == 0:
        break
    print()

    print("Question 3:")
    sleep(1.0)
    print("What is the highest grossing movie of all time?")
    sleep(1.0)
    print("A. Titanic")
    sleep(0.5)
    print("B. Spirited Away")
    sleep(0.5)
    print("C. Avatar")
    sleep(0.5)
    answer = input("Please enter your answer:")
    if answer != "C":
        print("Incorrect!")
    else:
        print("Correct")

    sleep(1.0)
    if my_timer == 0:
        break
    print()

    print("Question 4:")
    sleep(1.0)
    print("What is the smallest United State of America?")
    sleep(1.0)
    print("A. Rhode Island")
    sleep(0.5)
    print("B. Hawaii")
    sleep(0.5)
    print("C. Reddit")
    sleep(0.5)
    answer = input("Please enter your answer:")
    if answer != "C":
        print("Incorrect!")
    else:
        print("Correct")

    sleep(1.0)
    if my_timer == 0:
        break
    print()


print()
print("Time's Up!")
