class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            asa = target - nums[i]
            jj = i+1
            kk = nums[jj::]
            if asa in kk:
                j = kk.index(asa) + jj
                return [i, j]