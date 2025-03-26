from maqueen import *
from microbit import *

WHITE = 1
BLACK = 0
MOTOR_FORWARD = 0
MOTOR_BACKWARD = 1
SPEED = 38
DIRECTION_LEFT="left"
DIRECTION_RIGHT = "right"
SPEED_SLOW = 15
STOP = 0
DIRECTION_LEFT = "left"
DIRECTION_RIGHT = "right"
DIRECTION_FORWARD = "forward"
DIRECTION_BACKWARD = "backward"
dire= "horaire"
Go = 500

'''L1=0
 M=1
 R1=2
 L2=3
 R2=4'''

def parcours_labyrinthe(speed) :
    if line_sensor(0)==1:
        if line_sensor(1)== 1:
            motor_run(Motor.LEFT,speed,Direction.FORWARD)
            motor_run(Motor.RIGHT,speed,Direction.BACKWARD)
        elif line_sensor(1) == 0:
            motor_run(Motor.LEFT,speed,Direction.FORWARD)
            motor_run(Motor.RIGHT,speed,Direction.FORWARD)
    elif line_sensor(0)== 0:
            motor_run(Motor.LEFT,speed,Direction.BACKWARD)
            motor_run(Motor.RIGHT,speed,Direction.FORWARD)


while True:
    parcours_labyrinthe(SPEED)
