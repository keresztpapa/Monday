import time
from adafruit_servokit import ServoKit

# Initialize the servo hat
global kit
kit = ServoKit(channels=16)

def move_(angle_from, angle_to, motor_num):
# Set the initial position of the servo to 0 degrees
# Change this to the index of your servo
  kit.servo[motor_num].angle = angle_from

# Define the desired angle and speed
  speed = 1  # Change this to the desired speed (0 to 1)

# Calculate the pulse width based on the desired angle (150 to 600)
  pulse_width = int(150 + (angle_to / 180.0) * 450)

# Set the PWM frequency to 50Hz (standard for servos)
  kit._pca.frequency = 50

# Move the servo to the desired angle at the desired speed
  if angle_from < angle_to:
    while angle_from < angle_to:
      print(angle_from)
      angle_from += speed
      kit.servo[motor_num].angle = angle_from
  elif angle_from > angle_to:
    while angle_from > angle_to:
      print(angle_from)
      angle_from -= speed
      kit.servo[motor_num].angle = angle_from

def stand():
  kit.servo[0].angle = 90
  kit.servo[1].angle = 180
  kit.servo[2].angle = 180
  kit.servo[4].angle = 0
  kit.servo[5].angle = 0
  kit.servo[6].angle = 0
  kit.servo[8].angle = 0
  kit.servo[9].angle = 0
  kit.servo[10].angle = 0
  kit.servo[12].angle = 90
  kit.servo[13].angle = 180
  kit.servo[14].angle = 180

# REVERSED 2-3 bal also
#horizontal  90 -> 0
#move_(angle_from=0, angle_to=90, motor_num=0)
#move_(angle_from=0, angle_to=180, motor_num=1)
#move_(angle_from=0, angle_to=180, motor_num=2)

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
