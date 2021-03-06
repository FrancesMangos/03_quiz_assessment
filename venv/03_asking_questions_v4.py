import random
play_game = True

test_list = [["What is the most used streaming service?", "netflix", "disney+", "hulu", "a", "A"],
             ["What is the smallest planet in our solar system?", "mercury", "venus", "earth", "a", "A"],
             ["In which country did Lego originate from?", "germany", "england", "denmark", "c", "C"],
             ["What chases the player's character in Pacman?", "goblins", "ghosts", "inner demons and self doubt", "b", "B"]]

question = 1

random.shuffle(test_list)

while play_game == True and len(test_list) != 0:
    print("Question {}".format(question))
    print(test_list[0][0])
    print("A. {}".format(test_list[0][1]))
    print("B. {}".format(test_list[0][2]))
    print("C. {}".format(test_list[0][3]))
    guess = input("What is your answer?")
    if guess == test_list[0][4] or guess == test_list[0][5]:
        print("CORRECT!")
    else:
        print("INCORRECT. :(")
    del test_list[0]
    question += 1
    print()

play_game = False

if play_game == False:
    print("Game Over")
