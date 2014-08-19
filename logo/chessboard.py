from tealight.logo import move, turn

for i in range(0,4):
  n = 10
  while n < 90:
      move(n+(i*10))
      turn(90)
   
  
 