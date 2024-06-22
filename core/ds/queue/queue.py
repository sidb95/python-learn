class Queue1:
  def __init__(self):
    self.Q = []
  
  def insert(self, node):
    L = []
    L.append(node)
    for q in self.Q:
      L.append(q)
    self.Q = L
  
  def remove(self):
    self.Q.pop()
  
  def front(self):
    return self.Q[0]

  def back(self):
    size1 = len(self.Q)
    return self.Q[size1 - 1]

  def empty(self):
    return (self.Q == [])

