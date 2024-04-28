import sys
from common.common import *
import math

# test
def main(arg) -> float:
    if arg is None or arg == []:
        v = 100 # meter per second
    else:
        v = float(arg[0])

    theta = math.pi / 4 # 45 degrees for max distance, assuming no air resistance
    g = 9.81


    #vy = 0.5 * g * t
    #vx = d / t
    #vy = 0.5 * g * d / vx
    #vy = v * math.sin(theta)
    #vx = v * math.cos(theta)

    d = (v ** 2) * (2 * math.cos(theta) * math.sin(theta)) / g

    answer_dict = {
        'd': d,
        }

    for k, v in answer_dict.items():
        print(f"{k}: {v}")

    answer = d
    return answer

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
