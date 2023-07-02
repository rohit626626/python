#email find
import re

str='''
This is my school. amit@gmail.com It is out of the city. phone no is 357579567
There is a big hall. sonu@gmail.com There are playground
'''
email=re.findall(r"\w*@\S*\w",str)
print(email)