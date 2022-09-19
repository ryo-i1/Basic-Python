import math

def area(r):
    return r**2 * math.pi

def circ(r):
    return 2 * r * math.pi

r = float(input())
print("{:.6f} {:.6f}".format(area(r), circ(r)))

