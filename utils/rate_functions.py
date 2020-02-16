# some useful rate functions
import math

def easeOutBounce(t):
    if t < 1 / 2.75:
        return 7.5625 * t * t
    elif t < 2 / 2.75:
        c = t - 1.5/2.75
        return 7.5625 * c * c + 0.75
    elif t < 2.5 / 2.75:
        c = t - 2.25 / 2.75
        return 7.5625 * c * c + .9375
    else:
        c = t - 2.625 / 2.75
        return 7.5625 * c * c + .984375

def easeInBounce(t):
    return 1 - easeOutBounce(1 - t)

def easeInOutBounce(t):
    if t < 0.5:
        return easeInBounce(2 * t)
    else:
        return easeOutBounce(2 * t - 1)
    
def easeOutElastic(t):
    s, a = 1.70158, 1
    
    if t == 0: return 0
    if t == 1: return 1

    p = 0.3
    if a < 1:
        a, s = 1, p / 4
    else:
        s = p / (2 * math.pi) * math.asin(1 / a)

    return a * pow(2, -10 * t) * math.sin((t - s) * (2 * math.pi) / p) + 1
