def add(a,b):
    return a+b

if __name__=="__main__": #we are import namefun file in other file(nameother), nameother file print complete namefun file data
                         #it function hide namefile data in other file(nameother) 
                         # we import namefun and other file not access namefun file data
    ot=add(4,6)
    print(ot)