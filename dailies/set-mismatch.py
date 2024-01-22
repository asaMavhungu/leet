from typing import List

class Solution:
	def findErrorNums(self, nums: List[int]) -> List[int]:
		
		size = len(nums)
		
		asa = [0] * (size+1)

		total = (size * (size+1))//2

		count = 0

		ans = [-1, -1]

		for num in nums:
			
			if asa[num] == 0:
				asa[num] = num
				count += num
			else:
				ans[0] = num

		ans[1] = total - count
		return ans
		return asa, ans, count, total
	
sol = Solution()

liss = [1,2,2,4]

print(sol.findErrorNums(liss))