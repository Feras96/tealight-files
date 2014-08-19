from tealight.logo import move, turn

for i in range(1,100):
  n = 10
  while n < 90:
      move(n+(i*10))
      turn(90)
   
  
 