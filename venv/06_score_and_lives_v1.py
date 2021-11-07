import random
play_game = True

test_list = [["What is the most used streaming service?", "netflix", "disney+", "hulu", "a", "A"],
             ["What is the smallest planet in our solar system?", "mercury", "venus", "earth", "a", "A"],
             ["In which country did Lego originate from?", "germany", "england", "denmark", "c", "C"],
             ["What chases the player's character in Pacman?", "goblins", "ghosts", "inner demons and self doubt", "b", "B"]]

random.shuffle(test_list)

question = 1
score = 0
lives = 5
questions_answered = 0

while play_game == True and len(test_list) != 0 and lives > 0:
    print("Question {}".format(question))
    print(test_list[0][0])
    print("A. {}".format(test_list[0][1]))
    print("B. {}".format(test_list[0][2]))
    print("C. {}".format(test_list[0][3]))
    guess = input("What is your answer?")
    if guess == test_list[0][4] or guess == test_list[0][5]:
        print("CORRECT!")
        score += 10
        questions_answered += 1
    else:
        print("INCORRECT!")
        lives -= 1
        score += 5
    del test_list[0]
    question += 1
    print()

if lives == 0:
    print("All Lives Lost. Game Over")
    print("You answered {} questions correctly!".format(questions_answered))
    print("Your final score is: {}".format(score))
else:
    print("Game Over")
    print("You answered {} questions correctly!".format(questions_answered))
    print("Your final score is: {}".format(score))
