# HOMEWORK 3 --- ES2
# Bubble Level

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Sofia Levy
# NUMBER OF HOURS TO COMPLETE: 6
# YOUR COLLABORATION STATEMENT(s):
# I worked with Rene Jameson on this assignment.
# I received assistance from Dr. Cross on this assignment.

#*****************************************

import math
from microbit import *

def get_accel_x():  #returns the acceleration of x axis
    return accelerometer.get_x()
def get_accel_y():  #returns the acceleration of y axis
    return accelerometer.get_y()
def get_accel_z():  #returns the acceleration of z axis
    return accelerometer.get_z()

def get_radians_y(x, y, z): #returns the angle between y and z in radians
    x = get_accel_x()
    y = get_accel_y()
    z = get_accel_z()
    return math.atan2(y, math.sqrt(x**2 + z**2))

def get_radians_x(x, y, z): #returns the angle between x and z in radians
    x = get_accel_x()
    y = get_accel_y()
    z = get_accel_z()
    return math.atan2(x, math.sqrt(y**2 + z**2))

def get_degrees_y(x, y, z): #returns the angle between y and z in degrees
    return ((get_radians_y(x, y, z)*180)/math.pi)

def get_degrees_x(x, y, z): #returns the angle between x and z in degrees
    return((get_radians_x(x, y, z)*180)/math.pi)

while True:
    sleep(100)

    x = get_accel_x()
    y = get_accel_y()
    z = get_accel_z()

    a_y = get_degrees_y(x, y, z)
    a_x = get_degrees_x(x, y, z)

    #print((a_x, a_y))

    if ((a_x >= -5 and a_x < 5) and (a_y >= -5 and a_y < 5)):   #displays happy face when microbit is approximatley level
        display.show(Image.HAPPY)
    elif ((a_x <= 90 and a_x > 45) and (a_y >= -5 and a_y < 5)):    #displays east arrow when microbit tilted east
        display.show(Image.ARROW_E)
    elif ((a_x >= -90 and a_x < -45) and (a_y >= -5 and a_y < 5)):  #displays west arrow when microbit tilted west
        display.show(Image.ARROW_W)
    elif ((a_x >= -5 and a_x < 5) and (a_y <= 90 and a_y > 45)):    #displays south arrow when microbit tilted south
        display.show(Image.ARROW_S)
    elif ((a_x >= -5 and a_x < 5) and (a_y >= -90 and a_y < -45)):  #displays north arrow when microbit tilted north
        display.show(Image.ARROW_N)
    elif ((a_x <= 45 and a_x >= 5) and (a_y <= 45 and a_y >= 5)):   #displays southeast arrow when microbit tilted southeast
        display.show(Image.ARROW_SE)
    elif ((a_x <= 45 and a_x >= 5) and (a_y >= -45 and a_y < -5)):  #displays northeast arrow when microbit tilted northeast
        display.show(Image.ARROW_NE)
    elif ((a_x >= -45 and a_x < -5) and (a_y <= 45 and a_y >= 5)):  #displays southwest arrow when microbit tilted southwest
        display.show(Image.ARROW_SW)
    elif ((a_x >= -45 and a_x < -5) and (a_y >= -45 and a_y < -5)): #displays northwest arrow when microbit tilted northwest
        display.show(Image.ARROW_NW)
    else:
        None