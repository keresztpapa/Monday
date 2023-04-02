import time
from adafruit_servokit import ServoKit

def move_(angle_from, angle_to, motor_num):
  # Initialize the servo hat
  kit = ServoKit(channels=16)

# Set the initial position of the servo to 0 degrees
# Change this to the index of your servo
  kit.servo[motor_num].angle = 0

# Define the desired angle and speed
  speed = 1  # Change this to the desired speed (0 to 1)

# Calculate the pulse width based on the desired angle (150 to 600)
  pulse_width = int(150 + (angle_to / 180.0) * 450)

# Set the PWM frequency to 50Hz (standard for servos)
  kit._pca.frequency = 50

# Move the servo to the desired angle at the desired speed

  while angle_from < angle_to:
    print(angle_from)
    angle_from += speed
    kit.servo[motor_num].angle = angle_from

#time.sleep(0.05)  # Adjust the delay to control the speed
  time.sleep(1)
#  kit.servo[motor_num].angle = 0


move_(angle_from=0, angle_to=0, motor_num=2)

