class Solution:

	def isValid(self, s: str) -> bool:
		hash: dict = { '(':')', '[': ']', '{':'}' }
		stack: list = []
		for char in s:
			if stack and char == stack[-1]:
				stack.pop()
			elif char in hash.keys():
				stack.append(hash[char])
			else:
				return False
		return stack == []
	

asa: Solution = Solution()
s: str = "]"

print(asa.isValid(s))