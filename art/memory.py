from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

print "This is art mode!"

print screen_width
print screen_height

background("paper.jpg")

x = 0
y = 150

width = 8      
height = 6

for i in range(0,height):
  for j in range(0,width):
      image(x + i * 60, y + j * 60, "misc/Card.png")
text(screen_width/2 - 50, 100, "Memory Game!")


lastx = None
lasty = None
hue = 0

def handle_mousemove(x,y):
  global lastx, lasty, hue
  
  line(lastx or x, lasty or y, x, y)
  color("hsl(%d,100%%,50%%)" % hue)
  
  hue += 1
  
  lastx = x
  lasty = y
  
