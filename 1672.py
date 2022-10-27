from typing import *

class Solution:
	def maximumWealth(self, accounts: List[List[int]]) -> int:
		acc = [sum(i) for i in accounts]
		return max(acc)
