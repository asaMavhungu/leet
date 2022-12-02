from typing import List
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		turtoise = 1
		for i in range(1, len(nums)):
			if nums[i] > nums[turtoise-1]:
				nums[turtoise] = nums[i]
				turtoise += 1
		return turtoise

asa = Solution()
k = asa.removeDuplicates([0,1,1,1,1,1,1,2,2,2,3,3,3,3,3,4])
print(k)