import csv
import random
import re
import math

class Pozycja2d():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Wiesiu():
    def __init__(self, udzwig, maxPojemnosc):
        self.maxUdzwig = int(udzwig)
        self.maxPojemnosc = int(maxPojemnosc)
        self.waga=0
        self.pojemnosc=0
        self.pelnyWozek=False
        self.pozycja=Pozycja2d(0,0)
        self.przebieg = 0
        self.inv = []
        self.historia = []

    def podniesZlom(self, Zlom):
        #wiesiu: sprawdzam czy dam rade go podniesc
        if(Zlom.waga + self.waga > self.maxUdzwig):
            return False
        if (Zlom.pojemnosc + self.pojemnosc > self.maxPojemnosc):
            return False
        #wiesiu: przecodze w nowe miejsce, naliczam przebieg
        staraPozycja = self.pozycja
        self.pozycja = Zlom.pozycja
        self.przebieg += math.sqrt((abs(staraPozycja.x)-abs(Zlom.pozycja.x))**2+(abs(staraPozycja.y)-abs(Zlom.pozycja.y))**2)
        # wiesiu: podnosze zlom
        self.waga += Zlom.waga
        self.pojemnosc += Zlom.pojemnosc
        self.inv.append(Zlom)

        return True

    def sprzedajZlom(self):
        #wiesiu: ide na zlomowisko(pozycja startowa[0,0])
        self.przebieg += math.sqrt((abs(self.pozycja.x)) ** 2 + (abs(self.pozycja.y) ** 2))
        self.pozycja = Pozycja2d(0,0)

        #wiesiu: zrzucam zlom
        self.waga=0
        self.pojemnosc=0
        self.historia.append(self.inv)
        self.inv = []

class Zlom():
    def __init__(self, nazwa, waga, pojemnosc, x, y):
        self.nazwa = nazwa
        self.waga = int(waga)
        self.pojemnosc = int(pojemnosc)
        self.pozycja = Pozycja2d(x,y)

    def toString(self):
        return self.nazwa +", waga:" + str(self.waga) +", pojemnosc:" + str(self.pojemnosc) + ", pozycja:[" + str(self.pozycja.x) +","+ str(self.pozycja.y)+"]"

#wczytywanie zlomu
file = open("zlom.csv")
csvreader = csv.reader(file)
dane = []
pattern = r'[\[\]\']'

for row in csvreader:
    if(row.__str__() != "[]"):
        row = re.sub(pattern, '', row.__str__())
        chunks = row.__str__().split(',')
        dane.append(Zlom(chunks[0], int(chunks[1]), int(chunks[2]), int(chunks[3]), int(chunks[4])))
file.close()


#narodziny wieslawa
wieski = []
for i in range(0,10):
    wieski.append(Wiesiu(100,1000))



for i in range(0,10):
    print("----------------------------")
    #zbieranie zlomu
    while(dane.__len__()>0):
        for i in range(0,10):
            los = random.randrange(0,dane.__len__(),1)
            if (wieski[0].podniesZlom(dane[los])):
    
                dane.pop(los)
            if(dane.__len__()==0):
                break
    
        wieski[0].sprzedajZlom()
    
    
    #wyswietlanie
    print("\nprzebieg: "+str(wieski[0].przebieg))
    
    for row in wieski[0].historia:
        for val in row:
            print(val.nazwa+" "+str(val.waga))
        print("\n")
    






