from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

if touch() =='Wall':
  turn()
if touch()!='Wall':
  move()

  