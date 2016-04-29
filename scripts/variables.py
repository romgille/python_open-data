from pathlib import Path

ORIGINPATH = Path('.')

# Data folder
DATAPATH = Path(ORIGINPATH / 'data/')
CSVDISTANCE = str(DATAPATH) + "/" + "distance.csv"
CSVAIRLINE = str(DATAPATH) + "/" + "airlines.csv"
CSVAIRPORT = str(DATAPATH) + "/" + "airports.csv"
CSVCOUNTRY = str(DATAPATH) + "/" + "countries.csv"
CSVROUTES = str(DATAPATH) + "/" + "routes.csv"
CSVLOCALISATION = str(DATAPATH) + "/" + "localisation.csv"

# Rapport folder
RAPPORTPATH = Path(ORIGINPATH / 'rapport/')

# Histo folder
HISTOPATH = Path(ORIGINPATH / 'histogramme/')
HISTO = str(HISTOPATH) + "/" + "histo.png"

# Map folder
MAPPATH = Path(ORIGINPATH / 'map/')
CARTE = str(MAPPATH) + "/" + "map.png"
