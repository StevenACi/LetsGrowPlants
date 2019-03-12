import pygame
import sys
import Objects
from game import plant


TreeAlive = True
TreeObject = Objects.Tree()

def main():
 pygame.init()
 clock = pygame.time.Clock()
 screen = pygame.display.set_mode((800,600))

 while True:
  trigger_next_cycle= False

  if TreeAlive:
   trigger_next_cycle = True

  for event in pygame.event.get():
   if (event.type == pygame.QUIT or
           (event.type == pygame.KEYDOWN and event.key == pygame.K_q)):    # end sim
    print("\n\n----END-SIM----")
    sys.exit(0)

   if trigger_next_cycle:
    screen.fill((255,255,255))   # clear screen to white
   TreeObject.update()
   pygame.display.flip()

 click.tick(10)

main()
