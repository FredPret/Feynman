import sys
from common.common import *


def main() -> float:
    # Earth
    earth_orbit_eccentricity = 0.0167
    #c_div_a = earth_orbit_eccentricity
    ra_div_rp = 1 / (1 + earth_orbit_eccentricity) - earth_orbit_eccentricity / (1 + earth_orbit_eccentricity)
    rp_div_ra = 1 / ra_div_rp

    answer_dict = {
        'earth_orbit_eccentricity': earth_orbit_eccentricity,
        'ra_div_rp': ra_div_rp,
        'rp_div_ra': rp_div_ra,
        }
    
    for k, v in answer_dict.items():
        print(f"{k}: {v}")

    answer = rp_div_ra
    
    return answer

if __name__ == '__main__':
    sys.exit(main())