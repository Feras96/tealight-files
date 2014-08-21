from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

print "This is art mode!"

print screen_width
print screen_height

background("paper.jpg")

x = 150
y = 150

width = 8   
height = 6


#Create grid of cards
for i in range(0,height):
  for j in range(0,width):
      image(x + i * 100, y + j * 100, "misc/Card.png")
      
      
text(screen_width/2 - 50, 100, "Memory Game!")


lastx = 0
lasty = 0


def handle_mousemove(x,y,button):
  global lastx, lasty
  
  if button == "left"
  lastx = x
  lasty = y
  
  
  
