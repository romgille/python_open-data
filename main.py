from scripts.variables import *
from scripts.fonctions import *
from scripts.histo import histogram
from scripts.carte import map

# Creation des fichiers csv

createCsvDistance()
createCsvLocalisationRoute()


# Creation de l'histogramme

histogram()


# Creation de la map

map()