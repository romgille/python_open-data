import numpy as np
import csv
from collections import namedtuple


def tri_airports(csvfile):

    # Dictionnaire
    dictio = {}

    with open(csvfile, 'r') as myfile:
        r = csv.reader(myfile, delimiter=',')
        next(r, None)   # permet de ne pas prendre la derniere ligne du fichier
        l = list(r)

# on veut la colonne 1 et 7

        ID = namedtuple('ID', ['Ville', 'Pays', 'Lat', 'Long', 'Contient'])
        for i in l:
            valeur = ID(i[2], i[3], (i[6]), (i[7]), i[10])
            dictio[i[4]] = valeur
        return dictio
        # return dictio


def tri_airlines(csvfile):

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
        return dictio        # return dictio


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

    return d  # retourne la distance orthodromique en mètres


def distance2Airports(csvfile, code1, code2):
    donnee = tri_airports(csvfile)
    lat1 = float(donnee[code1][2])
    lon1 = float(donnee[code1][3])
    lat2 = float(donnee[code2][2])
    lon2 = float(donnee[code2][3])
    print(orthodromie(lat1, lon1, lat2, lon2))
