# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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

class Solution:
  def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    Q = Queue1()
    Q.insert((root, 1))
    answer = 0
    level = 0
    maxVal = 0
    levelSum = 0
    prevNode = (root, 0)
    while (not Q.empty()):
      q = Q.front()
      val = q[1]
      if (val > prevNode[1]):
        if (maxVal < levelSum):
          maxVal = levelSum
          level = prevNode[1]
        levelSum = 0
      levelSum += q[0].val
      Q.remove()
      if (q[0].left is not None):
        Q.insert((q[0].left, val + 1))
      if (q[0].right is not None):
        Q.insert((q[0].right, val + 1))
      prevNode = q
    if (maxVal < levelSum):
      level = val
    return level

