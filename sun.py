###################################################################################
##################################################################################
##################################################################################
###################################################################################
##################################################################################

import random

class Sun:

 jeuls = 0
 mass = 0


 def __init__(self):
  self.jeuls = pow(1000,25)
  self.mass = pow(2555,25)

 def fluxMatrix(self):
  fluxM = random.randrange(-255,255)
  flux = self.jeuls + (fluxM * 500)
  return flux

 def update(self):
  self.fluxMatrix()
