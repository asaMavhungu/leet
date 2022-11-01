from typing import List

class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		x: List[int] = [len(i) for i in strs]
		y: int = min(x)
		z: List[str] = [ i[:y] for i in strs]

		a: str = z[0]
		for i in range(y):
			for j in z:
				if j[i] != a[i]:
					k = i
					return a[:i]
		return a

asa: Solution = Solution()
strs: List[str] = ["flower","flow","flight"]
one: str = asa.longestCommonPrefix(strs)
print(one)

