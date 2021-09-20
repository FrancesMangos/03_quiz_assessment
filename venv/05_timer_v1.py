import time
def countdown(t):
    while t>0:
        print(t)
        t = t - 5
        time.sleep(5)
    print("Time's Up!")

print("How many seconds to count down?")
seconds = input()
while not seconds.isdigit():
    print ("That wasn't an integer!")
    seconds = input()
seconds = int(seconds)
countdown(seconds)



