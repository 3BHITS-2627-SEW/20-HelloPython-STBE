# Fortsetzung des Cheat-Sheets

# importieren von bibliotheken
import numpy

# bennene ein Paket um:
import numpy as npy

# nur eine klasse aus einem Paket importieren
# und zusaetzlich umbennen
from numpy import number as npynb

# alles importieren
from numpy import *

# eigene Bibliotheken bzw. Pakete importieren
from mein_paket.meineKlasse import *

def main():
    number = numpy.sqrt(4)
    print("Wurzel aus 4:", number)
    number2 = npy.sqrt(16)
    print("Wurzel aus 16:", number2)
    # verwende number von npy
    #npy.number
    # verwende die Klasse Number, importiert via *
    #number.
    
    # Verwende die eigene Klasse:
    #MeineKlasse
    meinObjekt = MeineKlasse()
    print("Name vom Objekt:",meinObjekt.name)
    pass


if __name__ == "__main__":
    main()