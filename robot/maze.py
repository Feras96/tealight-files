from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
while touch() != 'wall':
  move()
  if touch() == 'wall':
    elif left_side == 'wall':
    turn(1)
    else turn(-1)
  

