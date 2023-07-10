import servo

def move_forward():
  while True:
    left_upper_step()
    left_lower_step()
    right_upper_step()
    right_lower_step()