from scripts.variables import *
from scripts.fonctions import *

tri_airlines(csvAirline)
tri_airports(csvAirport)
# print(orthodromie(48.85, 2.35, 40.717, -74))
print(distance2Airports(csvAirport, "LPY", "CDG"))