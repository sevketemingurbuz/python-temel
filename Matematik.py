class Matematik:
    def __init__(self, sayi1, sayi2):
        self.sayi1= sayi1
        self.sayi2= sayi2
    def topla(self):
        return self.sayi1 + self.sayi2
    def cikar(self):
        return self.sayi1 - self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2
        
matematik = Matematik(5,6)
sonuc = matematik.bol()
print(sonuc)

class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)
    def olasılık(self):
        self.sayi1 / (self.sayi1 + self.sayi2)
        
istatistik = Istatistik(3,5)
print(istatistik.topla())