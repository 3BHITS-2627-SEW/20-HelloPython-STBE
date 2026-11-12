# Erstelle eine Klasse in python
class MeineKlasse:
    # Konstruktor
    def __init__(self):
        # self in Python enspricht dem this-pointer in C++

        # name wird eine instanz-Variable
        self.__name = "EineKlasse"
        #pass # macht einfach gar nichts
    
    # eine Methode:
    def noNoneNovember(self): # sef ist immer die eigene instanz
        # hier waere der methoden-Rumpf

        # hier kommt der Rueckgabe-Part
        return("November!")

    # ein GETTER:
    def get_name(self) -> str:
        # hier ist der Zugriff auf __ - Private-Instanzvariablen moeglich
        return(self.__name)
    # ein SETTER:

    def set_name(self,neuer_name : str) -> None:
        # hier ist der Zugriff auf __ - Private-Instanzvariablen moeglich
        self.__name = neuer_name
        #pass