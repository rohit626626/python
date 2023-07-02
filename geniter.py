# iterable  __iter__() or __getitem__()
# iterator __next__
# iteration

#generator
def gen(n):
    for i in range(n):
        yield i

g=gen(5)
print(g.__next__())
print(g.__next__())
print(g.__next__())

s="hello"
for i in s:
    print(i)

