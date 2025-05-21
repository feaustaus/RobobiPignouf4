'''
Version: 0.1
Auteur(s)   : VN
Contact     : vincent.namy@edu.ge.ch
License     : "CC-BY-NC-SA"
Sources :
- https://github.com/lawther/maqueenplus/blob/main/maqueenplusv2.py
- https://github.com/DFRobot/pxt-DFRobot_MaqueenPlus_v20/blob/master/maqueenPlusV2.ts
'''


from microbit import pin0, pin1, pin2


class Servomotor:
    SERVO_P0 = 0
    SERVO_P1 = 1
    SERVO_P2 = 2
    

def gripper(servo_id, closingValue):
    '''
    Opens and close the maqueen V2 gripper
    ```
    gripper(Motor.Right, [(20, 1.28), (200, 1.22)])
    ```
    '''
    if closingValue < 0:
        closingValue = 0
    elif closingValue > 1:
        closingValue = 2
        
    angle = closingValue * (128-90) + 90

    if servo_id == Servomotor.SERVO_P0:
        pin0.write_analog(angle)
    elif servo_id == Servomotor.SERVO_P1:
        pin1.write_analog(angle)
    elif servo_id == Servomotor.SERVO_P2:
        pin2.write_analog(angle)