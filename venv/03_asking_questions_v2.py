incorrect_answers = 0
correct_answers = 0

answer_list = ["blue whale", "mercury", "netflix", "china"]

question_list = ["What is the biggest animal that has ever lived?",
                 "What is the smallest planet in our solar system?",
                 "What is the most popular streaming service?",
                 "Which country has the highest population?"]

while True:
    answer = input(question_list[0])
    answer = answer.lower()
    if answer == answer_list[0]:
        print("CORRECT!")
        correct_answers += 1
        break
    else:
        print("INCORRECT. TRY AGAIN")
        incorrect_answers += 1
while True:
    answer = input(question_list[1])
    answer = answer.lower()
    if answer == answer_list[1]:
        print("CORRECT!")
        correct_answers += 1
        break
    else:
        print("INCORRECT. TRY AGAIN")
        incorrect_answers += 1
while True:
    answer = input(question_list[2])
    answer = answer.lower()
    if answer == answer_list[2]:
        print("CORRECT!")
        correct_answers += 1
        break
    else:
        print("INCORRECT. TRY AGAIN")
        incorrect_answers += 1
while True:
    answer = input(question_list[3])
    answer = answer.lower()
    if answer == answer_list[3]:
        print("CORRECT!")
        correct_answers += 1
        break
    else:
        print("INCORRECT. TRY AGAIN")
        incorrect_answers += 1

print()
print("You got {} correct answers, and {} incorrect guesses.".format(correct_answers, incorrect_answers))
