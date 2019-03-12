import pygame

##where we draw the tree and everything
##tree like about the tree. for me,,
class Tree:
 position_x = 0
 position_y = 0
 screen = None
 color = (200,0,100)
 def __init__(self):

  if self.screen is None:
   self.screen = pygame.display.get_surface()

  ##we wil make these dynamic to the size of the window $$##
  self.position_x = 300
  self.position_y = 500



 def update(self):
  pygame.draw.rect(pygame.display.get_surface(), self.color, (self.position_x,self.position_y,20,-30))
