import random
import time

if __name__ == '__main__':
    random.seed(12)

    for i in range(10):
        print(random.randint(0, 10))
        time.sleep(0.5)
