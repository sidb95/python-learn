class Solution:
  def __init__(self):
    pass

  def gcd(a: int, b:int) -> int:
    if (a == 0):
      return b
    else:
      TEMP = a
      a = a % b
      b = TEMP
      return gcd(a, b)
