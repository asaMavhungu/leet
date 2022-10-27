from typing import *

class Solution:
	def numberOfSteps(self, num: int) -> int:
		n = 0
		while(num != 0):
			if num % 2 == 0:
				n += 1
				num = num//2
			else:
				n += 1
				num -= 1
		return n