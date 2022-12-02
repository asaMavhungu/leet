from typing import List
class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		found: int = 0
		for i in range(len(nums)):
			if nums[i] != val:
				nums[found] = nums[i]
				found += 1
		return found


asa = Solution()
k = asa.removeElement([0,1,2,2,3,0,4,2], 2)
print(k)