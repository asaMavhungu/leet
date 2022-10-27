class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num2 = target - nums[i]
            jj = i+1
            numList2 = nums[jj::]
            if num2 in numList2:
                j = numList2.index(num2) + jj
                return [i, j]