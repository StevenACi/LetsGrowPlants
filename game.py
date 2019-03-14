from Models import Stem as s
from Models import Root as r
import time as t
import Time
originTime = t.time()
elapsedTime = t.time()
from SaveData.FSave import SavePlant


## counting seconds using TimeSinceEpoch TSE ##
def timeframe():
 global elapsedTime
 global originTime
 elapsedTime = t.time()
 return elapsedTime

python_green = "#475042"

def main():
##time>>


# print(plant.prnt())
 print(originTime)
 global elapsedTime
 pater = Time.Time()
 #game loop
 while 1:
  elapsedTime = round(timeframe(),0)
  if not pater.plant.isDead :
   pater.update()
  else:
   print("Ad Astra...")
   exit(0)
  #SavePlant.save(plant)


  ##print(elapsedTime)
  t.sleep(1)
main()




