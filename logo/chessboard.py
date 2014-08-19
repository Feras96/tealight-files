from tealight.logo import move, turn

for i in range(0,100):
  n = 10 + (i*10)
  while n < 80:
    move(n)
    turn(90)
    move(10)
   
  
 