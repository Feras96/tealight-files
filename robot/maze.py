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
    elif left_side() != 'wall': 
      turn(-1)
    elif right_side() != 'wall':
      turn(1)
    elif left_side() and right_side() == 'wall':
      turn(2)
      
   
 

  

