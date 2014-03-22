import threading
import time
import sys

ThreadBreak = False
def QueuePopper():
    while not ThreadBreak:
        if len(queue) > 0:
            print queue.pop(0)
        else:
            time.sleep(5)

queue = []
threading.Thread(target=QueuePopper).start()

try:
    while True:
        in_chars = sys.stdin.readline()
        if in_chars != '\n':
            message = in_chars.rstrip()
            if message not in queue:
                queue.append(message)
except KeyboardInterrupt:
    ThreadBreak = True
    pass
