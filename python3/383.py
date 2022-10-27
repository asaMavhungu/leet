from typing import AnyStr

class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		m = [i for i in magazine]
		if len(magazine) < len(ransomNote):
			return False
		for i in ransomNote:
			if i in m:
				m.remove(i)
			else:
				return False
		return True
