import os
#print(os.getpid())

'''class Chintu():
    def a(self):
        print(5)

a=Chintu()
a.a()'''

class demo:
    def __init__(self,num):
        self.number= num
    
    def fun(self):
        print(self.number)
    
    def a(self):
        print(5)

    '''def __str__(self):
        return "Outright Length(%s, %s) " % (len(self.number), id(self))'''
    def __repr__(self):
        return "Length(%s, %s) " % (len(self.number), id(self))

b=demo('data')
print(b)
#b.fun()
#print(b)

