import sys
import math


def main() -> float:
    '''
    Arguments are how long a rocket accelerates at a given rate
    No air resistance
    Constant g
    t1 = duration of firing
    t2 = duration of coasting top max height
    t3 = duration of free-fall from max height
    '''


    # earth radius 
    earth_radius = 6371e3 # meters
    earth_circumference = 2 * math.pi * earth_radius # meters
    rotation_period = 24 * 60 * 60 # seconds
    rotation_speed = earth_circumference / rotation_period
    
    answer_dict = {
        'earth_circumference': earth_circumference,
        'rotation_period': rotation_period,
        'rotation_speed': rotation_speed,
    }

    for k, v in answer_dict.items():
        print(f"{k}: {v}")

    answer = f"The surface of Earth rotates at about {rotation_speed} m/s around a fixed point at its center"
    return answer

if __name__ == '__main__':
    sys.exit(main())
