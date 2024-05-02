import sys
from common.common import *


def main(arg) -> float:
    '''
    Arguments are how long a rocket accelerates at a given rate
    No air resistance
    Constant g
    t1 = duration of firing
    t2 = duration of coasting top max height
    t3 = duration of free-fall from max height
    '''
    print(arg)
    g = 9.806
    if arg is None or arg == []:
        t1 = 50 # seconds
        a = 2 * g
    else:
        t1 = float(arg[0])
        a = float(arg[1])

    # determine situation at end of firing
    vy1 = a * t1 # m/s
    sy1 = 0.5 * a * t1 ** 2 # meters - rocket starts from rest at position zero

    # find time between end of firing and top of arc
    '''
    vy2 = 0
    vy2 = -g*t2 + vy1
    t2 = (vy2 - vy1)/(-g)
    '''
    vy2 = 0
    t2 = (vy2 - vy1)/(-g)

    # determine rocket position at t1 + t2 
    sy2 = 0.5 * (-g) * t2 ** 2 + vy1 * t2 + sy1

    # determine time of free-fall from max height
    '''
    sy3 is the end position: the ground
    sy3 = 0
    sy3 = 0.5 * (-g) * t3 ** 2 + vy2 * t3 + sy2
    0.5 * g * t3 ** 2 = sy2
    t3 ** 2 = sy2 / (0.5 * g)
    t3 = (sy2 / (0.5 * g)) ** 0.5
    '''
    t3 = (sy2 / (0.5 * g)) ** 0.5

    
    answer_dict = {
        'vy1': vy1,
        'sy1': sy1,
        't2': t2,
        'sy2': sy2,
        't3': t3,
        }

    for k, v in answer_dict.items():
        print(f"{k}: {v}")

    answer = f"Max height: {numberize(sy2)} meters reached after {t1 + t2}s. Hits the ground again after {t1 + t2 + t3}s"
    return answer

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
