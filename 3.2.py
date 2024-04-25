import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from common import *


def main() -> float:
    # Earth
    earth_diameter = 12756 * 1e3 # meters
    earth_radius = earth_diameter / 2 # meters

    # Moon
    moon_period = 27.322*24*60*60 # seconds
    moon_semi_major_axis = (363300000+405500000)/2 # meters
    moon_t2_r3_ratio = moon_period ** 2 / moon_semi_major_axis ** 3

    # satellite
    satellite_t2_r3_ratio = moon_t2_r3_ratio
    satellite_perigee_above_surface = 225 * 1e3 # meters
    satellite_apogee_above_surface = 710 * 1e3 # meters
    satellite_perigee_above_core = satellite_perigee_above_surface + earth_radius # meters
    satellite_apogee_above_core = satellite_apogee_above_surface + earth_radius # meters
    satellite_semi_major_axis = (satellite_perigee_above_core + satellite_apogee_above_core) / 2 # meters
    satellite_t2 = satellite_t2_r3_ratio * satellite_semi_major_axis ** 3 # seconds ^ 2
    satellite_period_seconds = satellite_t2 ** 0.5 # seconds
    satellite_period_hours = satellite_period_seconds / (60*60) # hours

    answer_dict = {
        'earth_radius': earth_radius,
        'satellite_t2_r3_ratio': satellite_t2_r3_ratio,
        'satellite_perigee_above_surface': numberize(satellite_perigee_above_surface),
        'satellite_apogee_above_surface': numberize(satellite_apogee_above_surface),
        'satellite_perigee_above_core': numberize(satellite_perigee_above_core),
        'satellite_apogee_above_core': numberize(satellite_apogee_above_core),
        'satellite_semi_major_axis': numberize(satellite_semi_major_axis),
        'satellite_t2': satellite_t2,
        'satellite_period_seconds': numberize(satellite_period_seconds),
        'satellite_period_hours': numberize(satellite_period_hours),
        }
    
    for k, v in answer_dict.items():
        print(f"{k}: {v}")

    return satellite_period_hours

if __name__ == '__main__':
    sys.exit(main())