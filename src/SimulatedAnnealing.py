from structure.Structure import *
from parserfunc import *
import math
import random

def simulatedAnnealing(data):
  initialSol=data.generateRandomSol()
  tMin = 0.0001
  alpha = 0.9
  t = 1
  currentSol = initialSol

  while t > tMin:
    #print('new it')
    for i in range(100):
      currentEval = data.evaluation(currentSol)
      newSol = neighbourFunc(data,currentSol)
      newEval = data.evaluation(newSol)
      if newEval >= currentEval:
        #print("better func")
        currentSol = newSol
      else:
        var = -(currentEval - newEval)/10000000000
        #print(data.evaluation(currentSol) - data.evaluation(newSol))
        ap = math.pow(math.e, var/t)
        #print("AP VALUE:" + str(ap))
        rand = random.random()
        if ap > rand:
          print("VALUES: " + str(ap) + " "+  str(rand))
          currentSol = newSol
    t = t*alpha
  print("--------")
  currentSol.printVideosinCaches()
  print('ev:',data.evaluation(currentSol))

  return currentSol


#simulatedAnnealing()
#print("end function")

#data=readData("src/input/small.in")
#t0=time.perf_counter()
#simulatedAnnealing(data)
#t1=time.perf_counter()
#print(t1-t0)
