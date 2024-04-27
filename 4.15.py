import sys
from common.common import *

# test
def main() -> float:
    d = 22.5 # meters
    
    vy0 = 0
    vyend = 0

    g = -9.81

    
    #maxheight = vy0 + 0.5*g*tmaxy
    tmaxy = (maxheight - vy0) / (0.5*g)

    answer_dict = {
        'moon_g': moon_g
        }

    for k, v in answer_dict.items():
        print(f"{k}: {v}")

    answer = moon_g
    return answer

if __name__ == '__main__':
    sys.exit(main())
