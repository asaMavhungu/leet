def con(x: int) -> int:
	sum = 0
	while x > 0 :
		sum = sum * 10 + x%10
		x = x//10
	return sum
	
class Solution:
	def isPalindrome(self, x: int) -> bool:
		print(con(x))
		if x == con(x):
			return True
		return False
		
asa = Solution()
one = asa.isPalindrome(550)
print(one)