from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
if touch() != 'Wall':
  move()
  
if touch() =='Wall':
  turn(1)

