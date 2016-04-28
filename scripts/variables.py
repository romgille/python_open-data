from pathlib import Path

originPath = Path('.')

# Data folder
dataPath = Path(originPath / 'data/')
csvDistance = str(dataPath) + "/" + "distance.csv"
csvAirline = str(dataPath) + "/" + "airlines.csv"
csvAirport = str(dataPath) + "/" + "airports.csv"
csvCountries = str(dataPath) + "/" + "countries.csv"
csvRoutes = str(dataPath) + "/" + "routes.csv"
rapportPath = Path(originPath / 'rapport/')
histoPath = Path(originPath / 'histogramme/')
histo = str(histoPath) + "/" + "histo.png"
