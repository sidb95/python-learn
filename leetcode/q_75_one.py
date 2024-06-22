class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    answer = []
    size1 = len(nums)
    #
    prod = 1
    #
    for i in range(0, size1):
      prod *= nums[i]
    for i in range(0, size1):
      count1 = 0
      count2 = 0
      while (count1 != abs(prod)):
        count1 += nums[i]
        count2 += 1
      if (prod < 0 and nums[i] < 0):
        answer.append(count2)
      elif (prod > 0 and nums[i] > 0):
        answer.append(count2)
      else:
        answer.append((-1) * count2)
    return answer

