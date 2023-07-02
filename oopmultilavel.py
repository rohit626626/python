# multilavel inheritance child claas access parent class property 
class Dad:
    cricket=3
    def iscricket(self):
        return f"I am play cricket {self.cricket} formet"

class Son(Dad):
    dance=2
    def isdance(self):
        return f"I am  dancing {self.dance} type"

class Grandsun(Son):
    singer=2
    def issinger(self):
        return f"I am singing song {self.singer} language"

amit=Dad()
sumit=Son()
nitin=Grandsun()

print(nitin.iscricket())
print(nitin.cricket)
print(nitin.isdance())
print(nitin.issinger())

