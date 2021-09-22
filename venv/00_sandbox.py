from time import *
import threading

def countdown():
    global my_timer

    my_timer = 20

    for x in range(5):
        my_timer = my_timer - 1
        sleep(1)

    print("Time's Up")

countdown_thread = threading.Thread(target = countdown)

countdown_thread.start()

score = 0
incorrect_answers = 0
correct_answers = 0
play_game = True

answer_one = 'blue whale'
answer_two = "mercury"
answer_three = "netflix"
answer_four = "china"

while my_timer > 0:
    while play_game == True:
        answer = input("What is the biggest animal that has ever lived?")
        answer = answer.lower()
        if answer == answer_one:
            print("CORRECT!")
            correct_answers += 1
            break
        else:
            print("INCORRECT. TRY AGAIN")
            incorrect_answers += 1

    while play_game == True:
        answer = input("What is the smallest planet in our solar system?")
        answer = answer.lower()
        if answer == answer_two:
            print("CORRECT!")
            correct_answers += 1
            break
        else:
            print("INCORRECT. TRY AGAIN")
            incorrect_answers += 1

    while play_game == True:
        answer = input("What is the most popular streaming service?")
        answer = answer.lower()
        if answer == answer_three:
            print("CORRECT!")
            correct_answers += 1
            break
        else:
            print("INCORRECT. TRY AGAIN")
            incorrect_answers += 1

    while play_game == True:
        answer = input("Which country has the highest population?")
        answer = answer.lower()
        if answer == answer_four:
            print("CORRECT!")
            correct_answers += 1
            break
        else:
            print("INCORRECT. TRY AGAIN")
            incorrect_answers += 1

if my_timer == 0:
    play_game == False

print("You got {} correct answers, and {} incorrect guesses.".format(correct_answers, incorrect_answers))

