from tealight.art import (color, line, spot, circle, box, image, text, background)

class Cards(object):
  name = ""
  rank = 0
  
  def __init__(self, name, rank):
    self.name = name
    self.rank = rank
    
def Show_cards(name, rank):
  Card_shown = Cards(name , rank)
  return Card_shown