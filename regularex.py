#regulare expression search string in given data and print match string
import re

mystr='''Nehru Yuva Kendra Sangathan (NYKS) is an autonomous body of the Ministry of Youth Affairs & Sports, 
Government of India.It mobilizes youth through Youth Clubs
and involves them in nation building activities and inculcate in them such values
and skills that they become productive and responsible citizens of a modern, secular, democratic & technological India. 
Presently NYKS has 623 district offices called Nehru Yuva Kendra and 29 State Offices across the country. 
Nehru Yuva Kendra is headed by a district level officer called District Youth Coordinator.
Phone No is 34532-2390 and more info calling now.'''

patt=re.compile(r,"Clubs") #print item position and item for ex Clubs position(300,305) and name Clubs
patt=re.compile(r,".invo") #print item full name start with invo for ex innv full name is innolves
patt=re.compile(r,"^Nehru") #print string start Nehru
patt=re.compile(r,"Coordinator$") #print string end Coordinator
patt=re.compile(r,"in*") #print i and zero, one, more n
patt=re.compile(r,"in+") #print i and one, more n
patt=re.compile(r,"in{2}") #print only in
patt=re.compile(r,"(in){2}") #print in group
patt=re.compile(r,"(in){1}|Yuva") #print in,Yuva and both

patt=re.compile(r,"\ANehru") #print str start Nehru
patt=re.compile(r,"\bGoverment") #print line start Nehru
patt=re.compile(r,"Coordinator\b") #print line end Coordinator

patt=re.compile(r,"\d{5}-\d{4}") #print 5digit-4digit //phone number search for ex 34532-2390

matches=patt.finditer(mystr)
for match in matches:
    print(match)