from time import *
import threading

def countdown():
    global my_timer

    my_timer = 6

    for x in range(6):
        my_timer = my_timer - 1
        sleep(1)

    print()

answer_list = ["blue whale", "mercury", "netflix", "china"]

question_list = ["What is the biggest animal that has ever lived?",
                 "What is the smallest planet in our solar system?",
                 "What is the most popular streaming service?",
                 "Which country has the highest population?"]

incorrect_answers = 0
correct_answers = 0

countdown_thread = threading.Thread(target = countdown)

countdown_thread.start()

while my_timer > 0:

    print("QUESTION ONE")
    print(question_list[0])
    sleep(1.0)
    answer = input("What is your answer?")
    if answer == answer_list[0]:
        print("Correct!")
    else:
        print("Incorrect!")
    print()

    if my_timer == 0:
        break

    print("QUESTION TWO")
    print(question_list[1])
    sleep(1.0)
    answer_one = input("What is your answer?")
    if answer_one == answer_list[1]:
        print("Correct!")
    else:
        print("Incorrect!")

    if my_timer == 0:
        break


print("Time's Up!")
