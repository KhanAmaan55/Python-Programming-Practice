import time
from functools import lru_cache

@lru_cache(maxsize=3) #maxsize = n takes last n values as cache
def sleeping(n):
    """ Takes time to sleep """
    time.sleep(n)
    return n

if __name__ == "__main__":
    print("prosess is starting")
    sleeping(3)
    sleeping(2)
    sleeping(4)
    sleeping(1)
    print("Prosess Done!!!")
    print("again starting")
    sleeping(2)
    # sleeping(3)
    sleeping(1)
    sleeping(4)
    print("done")