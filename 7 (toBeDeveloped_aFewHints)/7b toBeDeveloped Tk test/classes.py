class A:
    a = 111

    def __init__(self,x):
        self.y = x

    def scrivi(self):
        self.a=222
        print self.y, A.a, self.a
        print globals()
        print locals()
        print vars(self)

a1 = A(15)
a2 = A(25)


a1.scrivi()
a2.scrivi()
