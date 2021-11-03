from time import *
import threading

def countdown():
    global my_timer

    my_timer = 10

    for x in range(10):
        my_timer = my_timer - 1
        sleep(1)

    print()

countdown_thread = threading.Thread(target = countdown)

countdown_thread.start()

while my_timer > 0:
    print("Ello there!")
    sleep(2.0)

print()
print("Time's Up!")
