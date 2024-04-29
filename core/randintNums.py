# randintNums
# sidb95
# bhatoresiddharth@gmail.com 
# 29th APR 2024

import random
import math

def __main__(m=10, n=20, l=5, rL=[]):
  for i in range(0, l):
    randVarA = random.randint(m, n)
    rL.append(randVarA)
  for i in range(0, l):
    print(rL[i])
    print("\n")

__main__(10, 20, 5, [])