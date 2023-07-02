#coroutines  //coroutines are searching data some time, we are search data next time then data print directly no use time 
def searcher():
    import time
    book="This is c language book"
    time.sleep(3)

    while True:
        text=(yield)
        if text in book:
            print("Your text in the book")
        else:
            print("Your text not in the book")

search=searcher()
print("searching start")
next(search)
search.send("language") #this use three secound for searching data
input("press any key")
search.send("c") #this print directly no use three secound

