news="Aaj tak"
match="One day"
a="This is %s %s"%(news,match)
print(a)

#secound method
x="Hello world {0}{1}"
b=x.format(news,match)
print(b)

#third type
c=f"Hello {news} is {match} {4*2}" # fstring add string and varible in one line
print(c)