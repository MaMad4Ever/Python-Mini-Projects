from alive_progress import alive_bar
import time

total = 100

with alive_bar(total) as bar:
    for i in range(total):
        time.sleep(1)
        bar()
