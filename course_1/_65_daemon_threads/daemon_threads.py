import time
import threading

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"logged in for: {count} seconds")

x = threading.Thread(target=timer, daemon=True)
x.setDaemon(True)
x.start()
print(x.isDaemon())

answer = input("say anything to finish countdown: \n")