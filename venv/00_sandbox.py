import time

# timer counts down in ones

# ask user how many seconds the program should count down from
seconds = int(input("How many seconds do you want to count down from"))

# loop that counts backwards
for i in range(seconds):
    print(str(seconds - i) + " seconds remain")
    time.sleep(1)


