# assuming the planets all start lined up at the 12 o clock position and proceed along their orbits, determine their positions after x days. Plot the result
import sys
from common.common import *
import math


def main(arg) -> float:

    # see https://farside.ph.utexas.edu/teaching/celestial/Celestial/node34.html and https://farside.ph.utexas.edu/teaching/celestial/Celestial/img738.png for more details

    # semi-major axis
    mercury_a = 0.38709893
    venus_a = 0.72333199
    earth_a = 1.00000011
    mars_a = 1.52366231
    jupiter_a = 5.20336301
    saturn_a = 9.53707032
    uranus_a = 19.19126393
    neptune_a = 30.06896348
    pluto_a = 39.48168677

    # eccentricity
    mercury_e = 0.20563069
    venus_e = 0.00677323
    earth_e = 0.01671022
    mars_e = 0.09341233
    jupiter_e = 0.04839266
    saturn_e = 0.05415060
    uranus_e = 0.04716771
    neptune_e = 0.00858587
    pluto_e = 0.24880766

    # inclination to ecliptic
    mercury_inclination_deg = 7.00487
    venus_inclination_deg = 3.39471
    earth_inclination_deg = 0.00005
    mars_inclination_deg = 1.85061
    jupiter_inclination_deg = 1.30530
    saturn_inclination_deg = 2.48446
    uranus_inclination_deg = 0.76986
    neptune_inclination_deg = 1.76917
    pluto_inclination_deg = 17.14175

    # longitude of ascending node
    mercury_omega_deg = 48.33167
    venus_omega_deg = 76.68069
    earth_omega_deg = -11.26064
    mars_omega_deg = 49.57854
    jupiter_omega_deg = 100.55615
    saturn_omega_deg = 113.71504
    uranus_omega_deg = 74.22988
    neptune_omega_deg = 131.72169
    pluto_omega_deg = 110.30347

    # longitude of perihelion
    mercury_perihelion_deg = 77.45645
    venus_perihelion_deg = 131.53298
    earth_perihelion_deg = 102.94719
    mars_perihelion_deg = 336.04084
    jupiter_perihelion_deg = 14.75385
    saturn_perihelion_deg = 92.43194
    uranus_perihelion_deg = 170.96424
    neptune_perihelion_deg = 44.97135
    pluto_perihelion_deg = 224.06676

    # mean longitude
    mercury_mean_longitude_deg = 252.25084
    venus_mean_longitude_deg = 181.97973
    earth_mean_longitude_deg = 100.46435
    mars_mean_longitude_deg = 355.45332
    jupiter_mean_longitude_deg = 34.40438
    saturn_mean_longitude_deg = 49.94432
    uranus_mean_longitude_deg = 313.23218
    neptune_mean_longitude_deg = 304.88003
    pluto_mean_longitude_deg = 238.92881



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))