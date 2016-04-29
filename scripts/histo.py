# Import Lib
import matplotlib.pyplot as plt
# Imports perso
from scripts.fonctions import csvToList
from scripts.variables import HISTO
from scripts.variables import CSVDISTANCE


def histogram():
    liste = csvToList(CSVDISTANCE)
    ordonnee = []
    for i in range(0, len(liste)):
        if liste[i][2] != '':
            ordonnee.append(float(liste[i][2]))
    abscisse = list(range(1000000, 10000000, 20000))
    plt.hist(ordonnee, abscisse)
    plt.xlabel('Distance orthodromique (en m)')
    plt.ylabel('Nombre de vols')
    plt.title('Nombre de vols par distance')
    plt.savefig(HISTO)
    plt.clf()
