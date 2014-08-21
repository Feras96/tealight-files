from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

print "This is art mode!"

print screen_width
print screen_height

background("paper.jpg")

x = 150
y = 150

width = 6   
height = 8


#Create grid of cards
for i in range(0,height):
  for j in range(0,width):
      image(x + j * 100, y + i * 100, "misc/Card.png")
      print (x + j * 100, y + i * 100)

#Title      
text(screen_width/2 - 50, 100, "Memory Game!")


lastx = 0
lasty = 0

#Click detection and card identification
def handle_mousedown(x,y,button):
  global lastx, lasty
  
  if button == "left":
    #print (x,y)
    lastx = x
    lasty = y
    a = (lastx - 150)/100
    b = (lasty - 150)/100
    #print lastx
    #print a
    #print b
    v = b * 100 + a
    print "Cell: (%d, %d), n: %d" % (a,b,v)
    

  
  
  
