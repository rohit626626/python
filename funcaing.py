import time
from functools import lru_cache

@lru_cache(maxsize=3) # lru_cache first time delay 3 secound and next time using nodelay, 
                       #we are use this function diffrent place, it no delay // maxsize save latest 3 item
                      
def somework(n):
    time.sleep(n)
    return n

if __name__=="__manin__":
    somework(3)
    print("calling")
    somework(3)
    print("calling again")



    