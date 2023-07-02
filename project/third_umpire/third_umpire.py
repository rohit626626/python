#third umpire
import tkinter
import cv2
import PIL.Image, PIL.ImageTK
from functools import partial
import threading
import time
import imutils

stream=cv2.videoCapture("clip.mp4")
flag=True
def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")
    #play reverse
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(CAP_PROP_POS_FRAMES, frame1=speed)

    grabbed,frame=stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTK.PhotoImage(image=PIL.ImageTK.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(140,25, fill="green",font="Times 25 italic bold", text="Decision Panding")
    flag=not flag
def pending(decision):
    # 1. Decision pending
    frame=cv2.cvtColor(cv2.imread("pending.jpg"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame=PIL.ImageTK.PhotoImage(image=PIL.Image.fromarray(), anchor=tkinter.NW)
    canvas.image=frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    # 2. Wait 1 sec
    time.sleep(1)
    # 3. Sponsor image
    frame=cv2.cvtColor(cv2.imread("sponsor.jpg"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame=PIL.ImageTK.PhotoImage(image=PIL.Image.fromarray(), anchor=tkinter.NW)
    canvas.image=frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    # 4. Wait 1.5 sec
    time.sleep(1.5)
    # 5. Out/notout image
    if decision=="out":
        decisionImg="out.jpg"
    else:
        decisionImg="out.jpg"   
    frame=cv2.cvtColor(cv2.imread("decisionImg.jpg"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame=PIL.ImageTK.PhotoImage(image=PIL.Image.fromarray(), anchor=tkinter.NW)
    canvas.image=frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    # 6. Wait 1.5 sec

def out():
    thread=threading.Thread(target=pending, args="out")
    thread.daemon=1
    thread.start()
    print("Player is out")


def not_out(): 
    thread=threading.Thread(target=pending, args="not_out")
    thread.daemon=1
    thread.start()
    print("Player is not out")

SET_WIDTH=650
SET_HEIGHT=368 

window=tkinter.Tk()
window.title("Third umpire review")
cv_img=cv2.cvtColor(cv2.imread("img1.jpg"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window, width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.Image.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canves = canvas.create_image(0,0,anchor=tkinter.NW, image=photo)
canvas.pack()

btn=tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play, -25))
btn.pack()

btn=tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play,-2))
btn.pack()

btn=tkinter.Button(window, text="Next (fast)>>", width=50, command=partial(play, 25))
btn.pack() 

btn=tkinter.Button(window, text="Next (slow)>>", width=50, command=partial(play, 2))
btn.pack()

btn=tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()

btn=tkinter.Button(window, text="Give Not Out", width=50, command= not_out)
btn.pack()

window.mainloop() 

