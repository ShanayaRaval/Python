import math

def trig_values(angle):
    rad = math.radians(angle)  # convert degree to radians

    print("Sin:", math.sin(rad))
    print("Cos:", math.cos(rad))
    print("Tan:", math.tan(rad))

trig_values(30)