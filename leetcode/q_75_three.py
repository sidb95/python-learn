# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def __init__():
    self.answer = 0
  
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    if (root is None):
      return self.answer
    elif (root.left is None and root.right is None):
      if (root.val == targetSum):
        return self.answer + 1
      else:
        return self.answer
    elif (root.left is None):
      if (root.val == targetSum):
        self.answer += 1
        return self.pathSum(root.right, 0)
      else:
        return self.pathSum(root.right, targetSum - root.val)
    elif (root.right is None):
      if (root.val == targetSum):
        self.answer += 1
        return self.pathSum(root.left, 0)
      else:
        return self.pathSum(root.left, targetSum - root.val)
