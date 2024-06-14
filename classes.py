class Fruita():
    def __init__(self,atribut,maduració):
        self.atribut=atribut
        self.maduració=maduració
    def sabor(self):
        pass
    def color(self):
        pass
    def quesoc(self):
        print("Soc una fruita")
class Poma(Fruita):
    def sabor(self):
        print("Sep dolç")
    def color(self):
        print("Soc de color vermell")
    def quesoc(self):
        print("Soc una poma")
class Taronja(Fruita):
    def sabor(self):
        print("Sep àcid")
    def color(self):
        print("Taronja")
    def quesoc(self):
        print("Soc una taronja")
class Plàtan(Fruita):
    def sabor(self):
        print("Sep dolç")
    def color(self):
        print("Groc")
    def quesoc(self):
        print("Soc un plàtan")
class Meló(Fruita):
    def __init__(self, atribut, maduració ):
        self.atribut=atribut
        self.maduració=maduració
    def sabor(self):
        print("Sep dolç")
    def color(self):
        print("Verd i groc")
    def quesoc(self):
        print("Soc un meló")

#Pprincipal
def pclasses():        
    a = [Poma("Rodó","10"), 
        Taronja("Rodó","0,5"), 
        Plàtan("Curv", "7"),
        Meló("Ovalat", "30") ]
    for e in a:
        e.sabor()
        e.color()
        e.quesoc()