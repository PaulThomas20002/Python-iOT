class Myclass:
    def __init__(self,p,q):#can use the parameter p and q anywhere in the class by self.%
        self.x=p
        self.y=q
    def addtwo(self):
        c=self.x+self.y
        return c
    def subtwo(self):
        c=self.x-self.y
        return c
