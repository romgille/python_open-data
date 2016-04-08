import csv
from collections import namedtuple

def tri_airlines(csvfile):

    # Liste
    ordre = []

    # Dictionnaire
    dictio = {}

    with open('airlines.csv', 'r') as myfile:
        r = csv.reader(myfile, delimiter=',')
        next(r, None)    ## permet de ne pas prendre la derniere ligne du fichier
        l = list(r)
        # print(l[0][1])

## on veut la colonne 1 et 7

        Company = namedtuple('Company', ['Pays'])
        for i in l:
            valeur = Company(i[6])
            dictio[i[1]] = valeur
        print(dictio)
        # return dictio

tri_airlines('airlines.csv')
