from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 600
y = 400
vx = 0
vy = 0
ax = 0
ay = 0

power = 0.3
gravity = 0.1

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = -power - gravity
  elif key == "right":
    ax = power - gravity
  elif key == "up":
    ay = -power - gravity
  elif key == "down":
    ay = power - gravity
  elif key == "None":
    ay = gravity

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay - 0.2
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)
  
  