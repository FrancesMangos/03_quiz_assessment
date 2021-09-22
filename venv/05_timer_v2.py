from time import *
import threading

def countdown():
    global my_timer

    my_timer = 5

    for x in range(5):
        my_timer = my_timer - 1
        sleep(1)

    print()

countdown_thread = threading.Thread(target = countdown)

countdown_thread.start()

while my_timer > 0:
    print("help me")
    sleep(1)

print()
print("Time's Up!")
