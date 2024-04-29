import sys
from common.common import *

# test
def main() -> float:
    '''
    calculate g on the Moon
    '''
    # Earth
    earth_diameter = 12756 * 1e3 # meters
    earth_radius = earth_diameter / 2 # meters
    earth_moon_mass_ratio = 81.3
    earth_g = 9.81

    # moon
    moon_radius = 1738 * 1e3 # meters
    moon_g = ( (1 / earth_moon_mass_ratio) * (earth_radius / moon_radius)**2 ) * earth_g

    answer_dict = {
        'moon_g': moon_g
        }
    
    for k, v in answer_dict.items():
        print(f"{k}: {v}")

    answer = moon_g
    explanation = '''This is the acceleration in m/s due to gravity at the moon's surface:'''
    
    return f"{explanation}: {answer}"


if __name__ == '__main__':
    sys.exit(main())