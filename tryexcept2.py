try:
    f=open("file20.txt")

except Exception as e: #try block not run then exception block run
    print(e)

else:
    print("Print this info") #except block not run else block run

finally:
    print("Important msg") # finally block all condition run