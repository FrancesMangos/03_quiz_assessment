play_game = True

test_list = [["What is the most used streaming service?", "netflix", "disney+", "hulu"],
             ["What is the smallest planet in our solar system?", "mercury", "venus", "earth"],
             ["In which country did Lego originate from?", "denmark", "germany", "england"],
             ["What chases the player's character in Pacman?", "ghosts", "goblins", "inner demons and self doubt"]]

correct_answers = ["netflix", "mercury", "denmark", "ghosts"]

question = 1

lives = 3

while play_game == True:
    print("Question {}".format(question))
    print(test_list[0][0])
    print("A. {}".format(test_list[0][1]))
    print("B. {}".format(test_list[0][2]))
    print("C. {}".format(test_list[0][3]))
    guess = input("What is your answer?")
    if guess in correct_answers:
        print("CORRECT!")
    else:
        print("INCORRECT. ")
        lives -= 1
    del test_list[0]
    question += 1
    print()
    if lives == 0:
        play_game = False

if play_game == False:
    print("All Lives Lost. Game Over")