from typing import List
class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		left = 0
		right = len(nums) - 1
		mid = right//2
		while left <= right:
			mid = (left+right)//2
			if target < nums[mid]:
				right = mid - 1
			elif target > nums[mid]:
				left = mid + 1
			else: return mid
		return left
asa = Solution()
k = asa.searchInsert([1,3,5,6], 8)
print(k)