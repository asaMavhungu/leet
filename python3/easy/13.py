class Solution:
	def romanToInt(self, s: str) -> int:
			sum = 0
			dic: dict[str, int] = {
				'I' : 1,
				'V' : 5,
				'X' : 10,
				'L' : 50,
				'C' : 100,
				'D' : 500,
				'M' : 1000
			}
			sum: int = 0
			
			now: int = dic[s[0]]
			nex: int = 0

			for i in range(len(s)-1):
				nex: int  = dic[s[i + 1]]
				if nex > now:
					sum -= now
				else:
					sum += now
				now = nex
			sum += nex
			return sum