mystr="rohit is a good boy"
print(len(mystr))
print(mystr[::-1])

print(type(mystr)) #check type (int ,str,dict,float)

print(mystr.isalnum()) #check alpha numeric value
print(mystr.isalpha()) #check alpha  value
print(mystr.endswith("boy")) #check string end boy given true
print(mystr.count("i")) #count cheracter 
print(mystr.capitalize()) #str first char print upper case
print(mystr.upper()) #all str print upper case
print(mystr.lower()) #all str print lower case
print(mystr.find("is")) #find str position 
print(mystr.replace("is","are")) #replace str (is replace to are)