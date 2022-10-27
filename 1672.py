class Solution:
	def maximumWealth(self, accounts: List[List[int]]) -> int:
		rich = 0
		for i in accounts:
			net = sum(i)
			if net > rich:
				rich = net
		return rich