# Import Lib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
# Imports perso
from scripts.fonctions import csvToList
from scripts.variables import CARTE
from scripts.variables import CSVLOCALISATION

def map():
    print("Creation de la map")
    map = Basemap('lcc', resolution='i')
    map.bluemarble()
    liste = csvToList(CSVLOCALISATION)
    for i in range(0, len(liste)):
        print("Creation des routes :", round(((i/len(liste))*100), 2), "%")
        try:
            map.drawgreatcircle(float(liste[i][2]),
                                float(liste[i][1]),
                                float(liste[i][5]),
                                float(liste[i][4]),
                                linewidth=0.5, color=(float(liste[i][6]), 0, 0))
        except ValueError:
            pass
    print("Sauvegarde de la carte")
    plt.title("Carte des vols")
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    plt.savefig(CARTE)
    plt.clf()
