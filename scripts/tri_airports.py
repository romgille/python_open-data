import csv
from collections import namedtuple

def tri_airports(csvfile):

    # Liste
    ordre = []
    # Dictionnaire
    dictio = {}

    with open('airports.csv', 'r') as myfile:
        r = csv.reader(myfile, delimiter=',')
        next(r, None)    ## permet de ne pas prendre la derniere ligne du fichier
        l = list(r)

## on veut la colonne 1 et 7

        Name = namedtuple('Name', ['Ville', 'Pays', 'Lat', 'Long', 'Contient'])
        for i in l:
            valeur = Name(i[2], i[3], (i[6]), (i[7]), i[10])
            dictio[i[1]] = valeur
        print(dictio)
        # return dictio

tri_airports('airports.csv')
