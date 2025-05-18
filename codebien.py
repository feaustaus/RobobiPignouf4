''' Auteur(s)   : Zubair Commar, Fausto Neefjes
    Date        : 18 mai 2025
    Version     : finale
    Description : Projet de fin d'année pour faire sortir deux microbits l'un après l'autre d'un labyrinthe

'''

# Importations
from maqueen import *
from microbit import *
from gripper import*


# CONSTANTES
WHITE = 1
BLACK = 0
MOTOR_FORWARD = 0
MOTOR_BACKWARD = 1
SPEED = 38
SPEED_SLOW = 15
CONST = False
ultra = 100



# fonction qui permet au maqueen de sortir du labyrinthe en collant le mur gauche
def parcours_labyrinthe(speed) :
    if line_sensor(0)==1:
        motor_run(Motor.LEFT,speed,Direction.FORWARD)
    if line_sensor(1)== 1:
            motor_run(Motor.LEFT,speed,Direction.FORWARD)
            motor_run(Motor.RIGHT,speed,Direction.BACKWARD)
    elif line_sensor(1) == 0 and line_sensor(0)==1:
            motor_run(Motor.LEFT,speed,Direction.FORWARD)
            motor_run(Motor.RIGHT,speed,Direction.FORWARD)
    elif line_sensor(0)== 0:
            motor_run(Motor.LEFT,speed,Direction.BACKWARD)
            motor_run(Motor.RIGHT,speed,Direction.FORWARD)
            
# fonction expérimentale qui essaye d'attrapper le microbit du deuxième microbit           
def manoeuvre():
    sleep(1500)
    motor_run(Motor.LEFT,0,Direction.FORWARD)
    motor_run(Motor.RIGHT,0,Direction.FORWARD)
    sleep(1000)
    gripper(Servomotor.SERVO_P1, 0.8)
    sleep(1000)
    motor_run(Motor.LEFT,42,Direction.FORWARD)
    motor_run(Motor.RIGHT,8,Direction.BACKWARD)
    sleep(3700)
    motor_run(Motor.LEFT,20,Direction.FORWARD)
    motor_run(Motor.RIGHT,20,Direction.FORWARD)
    sleep(500)
    gripper(Servomotor.SERVO_P1, 1)
    sleep(500)
    motor_run(Motor.LEFT,0,Direction.BACKWARD)
    motor_run(Motor.RIGHT,0,Direction.BACKWARD)
    sleep(3000)
    motor_run(Motor.LEFT,38,Direction.BACKWARD)
    motor_run(Motor.RIGHT,38,Direction.BACKWARD)
    sleep(2000)
    motor_run(Motor.LEFT,0,Direction.FORWARD)
    motor_run(Motor.RIGHT,0,Direction.FORWARD)
    sleep(5000)

################################## Programme principal #########################
while True:
# permet de sortir le premier maqueen
    parcours_labyrinthe(SPEED)
# Si nécessaire, permet d'enclencher la manoeuvre    
    if button_a.get_presses():
        CONST = True 
    ultra = ultrasonic()
    print(ultra)
    if ultra < 27 and ultra >22 :
        if CONST == True:
            manoeuvre()


