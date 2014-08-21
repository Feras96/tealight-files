from tealight.art import (color, line, spot, circle, box, image, text, background)


#name = ["a", "b", "c"]
#rank = [1, 2]

#class Cards(object):
#  name = ""
#  rank = 0
#  
#  def __init__(self, name, rank):
#    self.name = name
#    self.rank = rank
    
#def Show_cards(name, rank):
#  Card_shown = Cards(name , rank)
#  return Card_shown

#print ("a", 2)

for i in range(0,height):
  for j in range(0,width):
      image(x + i * 100, y + j * 100, "misc/Card.png")
      