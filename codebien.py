from maqueen import *
from microbit import *
from gripper import*

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
        motor_run(Motor.LEFT,speed,Direction.FORWARD)
    if line_sensor(1)== 1:
            motor_run(Motor.LEFT,speed,Direction.FORWARD)
            motor_run(Motor.RIGHT,speed,Direction.BACKWARD)
    elif line_sensor(1) == 0:
            motor_run(Motor.LEFT,speed,Direction.FORWARD)
            motor_run(Motor.RIGHT,speed,Direction.FORWARD)
    elif line_sensor(0)== 0:
            motor_run(Motor.LEFT,speed,Direction.BACKWARD)
            motor_run(Motor.RIGHT,speed,Direction.FORWARD)
def pickup():
    gripper(Servomotor.SERVO_P1, 0.8)
    sleep(5000)
    gripper(Servomotor.SERVO_P1, 1)
    sleep(10000)
while True:
#     parcours_labyrinthe(SPEED)

    motor_run(Motor.LEFT,38,Direction.FORWARD)
    motor_run(Motor.RIGHT,38,Direction.FORWARD)
#     pickup()
    print(ultrasonic())
    if ultrasonic() < 27:
        sleep(1500)
        motor_run(Motor.LEFT,0,Direction.FORWARD)
        motor_run(Motor.RIGHT,0,Direction.FORWARD)
        sleep(1000)
        gripper(Servomotor.SERVO_P1, 0.8)
        motor_run(Motor.LEFT,50,Direction.FORWARD)
        motor_run(Motor.RIGHT,8,Direction.BACKWARD)
        sleep(3300)
        motor_run(Motor.LEFT,20,Direction.FORWARD)
        motor_run(Motor.RIGHT,20,Direction.FORWARD)
        sleep(1000)
        gripper(Servomotor.SERVO_P1, 1)
        motor_run(Motor.LEFT,0,Direction.FORWARD)
        motor_run(Motor.RIGHT,0,Direction.FORWARD)
        sleep(3000)
        motor_run(Motor.LEFT,38,Direction.BACKWARD)
        motor_run(Motor.RIGHT,38,Direction.BACKWARD)
        sleep(2000)
        motor_run(Motor.LEFT,0,Direction.FORWARD)
        motor_run(Motor.RIGHT,0,Direction.FORWARD)
        sleep(5000)
