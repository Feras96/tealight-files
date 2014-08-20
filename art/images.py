from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 0
y = 150

width = 8  
height = 20

for i in range(0,height + 1):
  for j in range(0,width + 1):
    if j % 4 == 0 and i % 4 == 0:
      image(x + i * 60, y + j * 60, "misc/YellowFlower.png")
    else:
      image(x + i * 60, y + j * 60, "misc/Clover.png")
     
