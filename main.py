import threading
import time


def main():
    print("ran")
    time.sleep(1)
    print("done")


x = threading.Thread(target=main, args=())
x.start()
print(threading.active_count())
