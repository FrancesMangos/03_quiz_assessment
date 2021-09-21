score = 0
incorrect_answers = 0
correct_answers = 0

answer_one = 'blue whale'
answer_two = "mercury"
answer_three = "netflix"

while True:
    answer = input("What is the biggest animal that has ever lived?")
    answer = answer.lower()
    if answer == answer_one:
        print ("CORRECT!")
        correct_answers += 1
        break
    else:
        print ("INCORRECT. TRY AGAIN")
        incorrect_answers += 1

while True:
    answer = input("What is the smallest planet in our solar system?")
    answer = answer.lower()
    if answer == answer_two:
        print("CORRECT!")
        correct_answers += 1
        break
    else:
        print ("INCORRECT. TRY AGAIN")
        incorrect_answers += 1

while True:
    answer = input("What is the most popular streaming service?")
    answer = answer.lower()
    if answer == answer_three:
        print("CORRECT!")
        correct_answers += 1
        break
    else:
        print ("INCORRECT. TRY AGAIN")
        incorrect_answers += 1

print("You got {} correct answers, and {} incorrect guesses.".format(correct_answers, incorrect_answers))

