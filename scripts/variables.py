from pathlib import Path

originPath = Path('.')

# Data folder
dataPath = Path(originPath / 'data/')
csvAirline = str(dataPath) + "/" + "airlines.csv"
csvAirport = str(dataPath) + "/" + "airports.csv"
csvCountries = str(dataPath) + "/" + "countries.csv"
csvRoutes = str(dataPath) + "/" + "routes.csv"
