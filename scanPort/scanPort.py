
import time
from .tools import scanPortTools

def main():
  start = time.time()

  target = input('Ip à scanner ?: ')
  rangeBegin = int(input('Premier numéro de port: '))
  rangeEnd = int(input('Dernier numéro de port: '))

  for x in range(rangeBegin, rangeEnd):
      if scanPortTools.pscan(x):
          end = time.time()
          print('Port', x, 'is open. Found in: ', (end - start), 'seconds')
          
      else:
          print('Port', x, 'is closed')


