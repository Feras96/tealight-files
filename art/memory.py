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

for i in range(0,height):
  for j in range(0,width):
      image(x + i * 100, y + j * 100, "misc/Card.png")
      

class Cards(object):
  name = ""
  rank = 0
  
  def __init__(self, name, rank):
    self.name = name
    self.rank = rank
    
def Show_cards(name, rank):
  Card_shown = Cards(name , rank)
  return Card_shown
 
text(screen_width/2 - 50, 100, "Memory Game!")


lastx = 0
lasty = 0


def handle_mousemove(x,y):
  global lastx, lasty, hue
  
  lastx = x
  lasty = y
  
