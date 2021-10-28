play_game = True

test_list = [["What is the most used streaming service?", "netflix", "disney+", "hulu"],
             ["What is the smallest planet in our solar system?", "mercury", "venus", "earth"],
             ["In which country did Lego originate from?", "denmark", "germany", "england"],
             ["What chases the player's character in Pacman?", "ghosts", "goblins", "inner demons and self doubt"]]

correct_answers = ["netflix", "mercury", "denmark", "ghosts"]

question = 1

while play_game == True and len(test_list) != 0:
    print("Question {}".format(question))
    print(test_list[0][0])
    print("a. {}".format(test_list[0][1]))
    print("b. {}".format(test_list[0][2]))
    print("c. {}".format(test_list[0][3]))
    guess = input("What is your answer?")
    if guess in correct_answers:
        print("CORRECT!")
    else:
        print("INCORRECT. :(")
    del test_list[0]
    question += 1
    print()

if len(test_list) == 0:
    print("Game Over")

