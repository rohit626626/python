#set contain unique value
s_from_list=set([1,2,3,4])
print(s_from_list)

s1=set()
s1.add(1)
s1.add(1) # no add 1 because 1 already add
s1.add(2)
print(s1)
print(min(s1)) #print min value
print(len(s1)) #print length
s2=({1,2,3,4})
s2.remove(4) #remove 4 in set
print(s1,s2)

print(s1.union(s2)) #union add all value in set
print(s1.intersection(s2)) #intersection given common value in s1 and s2 set
