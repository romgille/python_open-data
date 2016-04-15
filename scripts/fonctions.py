import numpy as np
import csv
from collections import namedtuple


def tri_airports(csvfile):

    # Liste
    ordre = []
    # Dictionnaire
    dictio = {}

    with open(csvfile, 'r') as myfile:
        r = csv.reader(myfile, delimiter=',')
        next(r, None)   # permet de ne pas prendre la derniere ligne du fichier
        l = list(r)

# on veut la colonne 1 et 7

        Name = namedtuple('Name', ['Ville', 'Pays', 'Lat', 'Long', 'Contient'])
        for i in l:
            valeur = Name(i[2], i[3], (i[6]), (i[7]), i[10])
            dictio[i[1]] = valeur
        print(dictio)
        # return dictio


def tri_airlines(csvfile):

    # Liste
    ordre = []

    # Dictionnaire
    dictio = {}

    with open(csvfile, 'r') as myfile:
        r = csv.reader(myfile, delimiter=',')
        next(r, None)   # permet de ne pas prendre la derniere ligne du fichier
        l = list(r)
        # print(l[0][1])

# on veut la colonne 1 et 7

        Company = namedtuple('Company', ['Pays'])
        for i in l:
            valeur = Company(i[6])
            dictio[i[1]] = valeur
        print(dictio)
        # return dictio


def orthodromie(lat1, lon1, lat2, lon2):
    earthRadius = 6371000
    radianlat1 = np.radians(lat1)
    radianlat2 = np.radians(lat2)
    diffradianlat = np.radians(lat2-lat1)
    diffradianlon = np.radians(lon2-lon1)
    sin2diffradianlat = np.sin(diffradianlat/2) * np.sin(diffradianlat/2)
    sin2diffradianlon = np.sin(diffradianlon/2) * np.sin(diffradianlon/2)
    cosradianlat12 = np.cos(radianlat1) * np.cos(radianlat2)

    a = sin2diffradianlat + cosradianlat12 * sin2diffradianlon
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    d = earthRadius * c

    return d

print(orthodromie(48.85, 2.35, 40.717, -74))
