import time
def countdown(t):
    while t>0:
        print(t)
        t = t - 5
        time.sleep(5)
    print("Time's Up!")

incorrect_answers = 0
correct_answers = 0

answer_one = 'blue whale'
answer_two = "mercury"
answer_three = "netflix"
answer_four = "china"

seconds = 20

seconds = int(seconds)
while seconds > 0:
    countdown(seconds)
    while True:
        answer = input("What is the biggest animal that has ever lived?")
        answer = answer.lower()
        if answer == answer_one:
            print("CORRECT!")
            correct_answers += 1
            break
        else:
            print("INCORRECT. TRY AGAIN")
            incorrect_answers += 1
    while True:
        answer = input("What is the smallest planet in our solar system?")
        answer = answer.lower()
        if answer == answer_two:
            print("CORRECT!")
            correct_answers += 1
            break
        else:
            print("INCORRECT. TRY AGAIN")
            incorrect_answers += 1
    while True:
        answer = input("What is the most popular streaming service?")
        answer = answer.lower()
        if answer == answer_three:
            print("CORRECT!")
            correct_answers += 1
            break
        else:
            print("INCORRECT. TRY AGAIN")
            incorrect_answers += 1
    while True:
        answer = input("Which country has the highest population?")
        answer = answer.lower()
        if answer == answer_four:
            print("CORRECT!")
            correct_answers += 1
            break
        else:
            print("INCORRECT. TRY AGAIN")
            incorrect_answers += 1

print("You got {} correct answers, and {} incorrect guesses.".format(correct_answers, incorrect_answers))
