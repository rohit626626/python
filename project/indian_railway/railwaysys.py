import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTs



def textToSpeech(text, filename):
    mytext=str(text)
    language="hi"
    myobj=gTTs(text=mytext,lang=language, slow=False)
    myobj.save(filename)



def mergAudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined 


def generateSkeleton():
    audio=AudioSegment.from_mp3("railway.mp3")
    # 1. kirpya dheyan dijiya 
    start=80000
    finish=90000
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    #2 .Is from city 


    # 3. Generate se chalkar 
    start=92000
    finish=99000
    audioProcessed=audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

     # 4. kirpya dheyan dijiya 


    # 5. Generate ke raaste
    start=110000
    finish=120000
    audioProcessed=audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6. is to city


    # 7. Generate ko jaane wali gaadi sakhya
    start=130000
    finish=140000
    audioProcessed=audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8. is train no and name 


    # 9. Generate kuch hi samay mei platform sankya
    start=150000
    finish=160000
    audioProcessed=audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10. is platform number


    # 11. Generate per aa rahi hai
    start=170000
    finish=180000
    audioProcessed=audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")



def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():

        #2 Generate from city
        textToSpeech(item["from"],"2_hindi.mp3")

        #4 Generate via city
        textToSpeech(item["via"],"4_hindi.mp3")

        #6 Generate to city
        textToSpeech(item["to"],"6_hindi.mp3") 

        #8 Generate train no and name
        textToSpeech(item["train_no"]+" "+item[train_name],"6_hindi.mp3")

        #10 Generate platform number
        textToSpeech(item["platform"],"10_hindi.mp3")

        audios=[f"(i)_hindi.mp3" for i in range(1,12)]

        announcement=mergeAudios(audios)
        announcement.export(f"announcement_{item[train_no]}_(index+1).mp3",formet="mp3")


if __name__ =="__main__":
    print("Generating Skelecton...")  
    generateSkeleton()
    print("Now Generating Announcment...")  
    generateAnnouncement("announce_hindi.xlsx")