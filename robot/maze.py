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
    if left_side() == 'wall':
      turn(1)
      move()
    if left_side() != 'wall': 
      turn(-1)
      move()
    
    
print left_side()
print right_side()