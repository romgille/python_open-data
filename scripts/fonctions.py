import numpy as np


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
