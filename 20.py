class Solution:

	def val(self, s: str) -> bool:
		if len(s)%2 == 1:
			return False
		if len(s) == 2:
			if ord(s[0]) - ord(s[-1]) not in [-1, -2]:
				return False
			return True
		for i in range(len(s)//2):
			if ord(s[i]) - ord(s[i+1]) in [-1, -2]:
				return self.val(s[:i] + s[i+2:])
		return False

	
	def isValid(self, s: str) -> bool:
		return self.val(s)
	

asa: Solution = Solution()
s: str = "()\{\}}{"
one: bool = asa.isValid(s)
print(one)