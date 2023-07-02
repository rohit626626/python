#health programe
from pygame import mixer
from datetime import datetime
from time import time
 
def musiconloop(file,stopper):
     mixer.init()
     mixer.music.load(file)
     mxier.music.play()
     while True:
         input_of_user=input()
         if input_of_user==stopper():
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n") 
     

if __name__=="__main__":
    musiconloop("water.mp3","stop")
    init_water=time()
    init_eyes=time()
    init_exercise=time() 
    watersec=5
    exsecs=10
    eyessecs=20

    while True:
        if time() - init_water>watersecs: 
            print("Water drinking time. Enter 'drank' to stop alarm. ")
            musiconloop("water.mp3","drank")
            init_water=time()
            log_now("Drank water at")
        
    while True:
        if time() - init_eyes>eyessecs: 
            print("Eye exercise time. Enter 'doneeyes' to stop alarm. ")
            musiconloop("eyes.mp3","doneeyes")
            init_eyes=time()
            log_now("Eyes relaxe at")
         
    while True:
        if time() - init_>exercise>exsecs: 
            print("Physical activity time. Enter 'donephy' to stop alarm. ")
            musiconloop("Physical activity.mp3","donephy")
            init_exercise=time()
            log_now("Physical activaty  at") 
    
