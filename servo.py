import time
from adafruit_servokit import ServoKit

# Initialize the servo hat
global kit
kit = ServoKit(channels=16)
# Set the PWM frequency to 50Hz (standard for servos)
kit._pca.frequency = 50

def wait(x):
  if x > 0:
    time.sleep(x/60*0.1)
  else:
    time.sleep(0.3)

def servo_move_and_wait(i, j):
  kit.servo[i].angle = j
  wait(j)

def stand():
  servo_move_and_wait(0, 90)
  servo_move_and_wait(1, 150)
  servo_move_and_wait(2, 150)
  servo_move_and_wait(4, 0)
  servo_move_and_wait(5, 30)
  servo_move_and_wait(6, 30)
  servo_move_and_wait(8, 0)
  servo_move_and_wait(9, 30)
  servo_move_and_wait(10, 30)
  servo_move_and_wait(12, 90)
  servo_move_and_wait(13, 150)
  servo_move_and_wait(14, 150)

def walk_forward():
#BAL-FELSO   horizontal :0 ::0->90       vertical: 1 ::180->90       leg: 2 ::180->90

#  servo_move_and_wait(1, 150)
  pass

#  servo_move_and_wait(1, 50)
#  servo_move_and_wait(6, 90)
#  servo_move_and_wait(5, 90)
#  servo_move_and_wait(10, 90)
#  servo_move_and_wait(9, 90)
#  servo_move_and_wait(14, 90)
#  servo_move_and_wait(13, 90)
#NORMAL
#move_(angle_from=90, angle_to=0, motor_num=4)
#move_(angle_from=90, angle_to=0, motor_num=5)
#move_(angle_from=90, angle_to=0, motor_num=6)

#NORMAL
#move_(angle_from=90, angle_to=0, motor_num=8)
#move_(angle_from=90, angle_to=0, motor_num=9)
#move_(angle_from=90, angle_to=0, motor_num=10)

# REVERSED 2-3 bal also
#horizontal  90 -> 0
#move_(angle_from=0, angle_to=90, motor_num=12)
#vertical
#move_(angle_from=90, angle_to=180, motor_num=13)
#leg
#move_(angle_from=180, angle_to=90, motor_num=14)


stand()
#walk_forward()
#stand()
