# Import Lib
import numpy as np
import csv
from collections import namedtuple
import matplotlib.pyplot as plt
# Import persos
from scripts.variables import *


def csvToList(csvfile):
    with open(csvfile, 'r') as myfile:
        reader = csv.reader(myfile, delimiter=',')
        next(reader, None)
        liste = list(reader)
    return liste


def tri_airports():
    dic = {}
    liste = csvToList(csvAirport)
    identifier = namedtuple('ID', ['Ville', 'Pays', 'Lat', 'Long', 'Contient'])
    for i in liste:
        valeur = identifier(i[2], i[3], (i[6]), (i[7]), i[10])
        dic[i[4]] = valeur
    return dic


def tri_airlines():
    dic = {}
    liste = csvToList(csvAirline)
    company = namedtuple('Company', ['Pays'])
    for i in liste:
        valeur = company(i[6])
        dic[i[1]] = valeur
    return dic


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

    return d  # retourne la distance orthodromique en metres


def distance2Airports(csvfile, code1, code2):
    donnee = tri_airports()
    # Ne pas prendre en compte les ID non valides.
    try:
        test = donnee[code1]
        test = donnee[code2]
    except KeyError:
        return
    lat1 = float(donnee[code1][2])
    lon1 = float(donnee[code1][3])
    lat2 = float(donnee[code2][2])
    lon2 = float(donnee[code2][3])
    return orthodromie(lat1, lon1, lat2, lon2)


def createCsvDistance():
    liste = csvToList(csvRoutes)
    with open(csvDistance, 'w', encoding='utf-8') as csvfile:
        csvVar = csv.writer(csvfile, delimiter=',')
        csvVar.writerow(["Depart", "Arrivee", "Distance"])
        for i in range(0, len(liste)):
            distance = distance2Airports(csvAirport, liste[i][2], liste[i][4])
            csvVar.writerow([liste[i][2], liste[i][4], distance])
            print(round(((i/67662)*100), 2), "%")
