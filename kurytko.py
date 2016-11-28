# -*- coding:utf-8 -*-

class Kura(object):
    """Kura"""
    def __init__(self, name):
        self.name = name
    def jedz(self, kuryto):
        kuryto.nasypane = 0

class Kuryto(object):
    """Kuryto"""
    def __init__(self):
        self.nasypane = 0
    def nasyp(self):
        self.nasypane = 1

class Kurnik(object):
    """Kurnik - zna swoje kury i kuryta"""
    def __init__(self):
        self.kury    = []
        self.kuryta  = []
    def dodaj_kure(self, kura):
        self.kury.append(kura)
    def dodaj_kuryto(self, kuryto):
        self.kuryta.append(kuryto)
    def get_kuryto(self):
        return self.kuryto
    def nasyp(self):
        for i in self.kuryta:
            i.nasyp()

if __name__ == '__main__':
    kurnik = Kurnik()
    kurnik.dodaj_kure(Kura("Zosia"))
    kurnik.dodaj_kure(Kura("Gosia"))
    kurnik.dodaj_kure(Kura("Cosia"))
    kurnik.dodaj_kuryto(Kuryto())
    kurnik.dodaj_kuryto(Kuryto())
    k0 = kurnik.kuryta[0]
    print k0.nasypane
    kurnik.nasyp()
    print k0.nasypane
    kurnik.kury[0].jedz(k0)
    print k0.nasypane







        
