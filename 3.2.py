import sys
from common.common import *


def main(arg) -> float:
    '''
    calculate the orbital period of a satellite given a perigee and apogee in meters. 
    Try it with 3.6e7 for both values!
    Geostationary height = 35,786 km
    '''

    if arg is None or arg == []:
        satellite_perigee_above_surface = 225 * 1e3 # meters
        satellite_apogee_above_surface = 710 * 1e3 # meters
    else:
        satellite_perigee_above_surface = float(arg[0])
        satellite_apogee_above_surface = float(arg[1])

    # Earth
    earth_diameter = 12756 * 1e3 # meters
    earth_radius = earth_diameter / 2 # meters

    # Moon
    moon_period = 27.322*24*60*60 # seconds
    moon_semi_major_axis = (363300000+405500000)/2 # meters
    moon_t2_r3_ratio = moon_period ** 2 / moon_semi_major_axis ** 3

    # satellite
    satellite_t2_r3_ratio = moon_t2_r3_ratio
    satellite_perigee_above_core = satellite_perigee_above_surface + earth_radius # meters
    satellite_apogee_above_core = satellite_apogee_above_surface + earth_radius # meters
    satellite_semi_major_axis = (satellite_perigee_above_core + satellite_apogee_above_core) / 2 # meters
    satellite_t2 = satellite_t2_r3_ratio * satellite_semi_major_axis ** 3 # seconds ^ 2
    satellite_period_seconds = satellite_t2 ** 0.5 # seconds
    satellite_period_hours = satellite_period_seconds / (60*60) # hours

    answer_dict = {
        'earth_radius': str(earth_radius) + ' [m]',
        'satellite_t2_r3_ratio': str(satellite_t2_r3_ratio),
        'satellite_perigee_above_surface': str(numberize(satellite_perigee_above_surface)) + ' [m]',
        'satellite_apogee_above_surface': str(numberize(satellite_apogee_above_surface)) + ' [m]',
        'satellite_perigee_above_core': str(numberize(satellite_perigee_above_core)) + ' [m]',
        'satellite_apogee_above_core': str(numberize(satellite_apogee_above_core)) + ' [m]',
        'satellite_semi_major_axis': str(numberize(satellite_semi_major_axis)) + ' [m]',
        'satellite_t2': str(satellite_t2) + ' [s**2]',
        'satellite_period_seconds': str(numberize(satellite_period_seconds)) + ' [s]',
        'satellite_period_hours': str(numberize(satellite_period_hours)) + ' [h]',
        }
    
    for k, v in answer_dict.items():
        print(f"{k}: {v}")

    answer = satellite_period_hours
    explanation = f'''This is the orbital period (in hours) for a sattelite with an apogee of {satellite_apogee_above_surface}m and a perigee of {satellite_perigee_above_surface}m'''
    
    return f"{explanation}: {answer}"

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
