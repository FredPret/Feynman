import sys
import math


def main() -> float:
    # a) speed of rotation relative to core
    earth_radius = 6371e3 # meters
    earth_circumference = 2 * math.pi * earth_radius # meters
    rotation_period = 24 * 60 * 60 # seconds
    rotation_speed_m_per_s = earth_circumference / rotation_period
    
    

    

    answer = ''
    answer += f"4.8a) The surface of Earth rotates at about {rotation_speed_m_per_s} m/s around a fixed point at its center\n"

    # b) angular velocity
    rotation_speed_rad_per_s = math.pi * 2 / rotation_period



    answer_dict = {
        'earth_circumference': earth_circumference,
        'rotation_period': rotation_period,
        'rotation_speed_m_per_s': rotation_speed_m_per_s,
        'rotation_speed_rad_per_s': rotation_speed_rad_per_s,
    }

    for k, v in answer_dict.items():
        print(f"{k}: {v}")

    answer += f"4.8b) The surface of Earth rotates at about {rotation_speed_rad_per_s} rad/s around a fixed point at its center\n"


    return answer

if __name__ == '__main__':
    sys.exit(main())
