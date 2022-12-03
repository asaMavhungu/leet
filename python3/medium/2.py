class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def makeLinkedList(l1):

	nodes = []
	for i in l1:
		nodes.append(ListNode(i))
	for i in range(len(nodes)-1):
		nodes[i].next = nodes[i+1]
	return nodes[0]


		
from typing import Optional
class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		
		head = mainPoint = ListNode()

		point1, point2 = l1, l2
		carry = 0
		while point1 or point2 or carry:
			val1 = val2 = 0
			
			if point1 != None:
				val1 = point1.val
				point1 = point1.next
			if point2 != None:
				val2 = point2.val
				point2 = point2.next

			sum = val1+val2+carry
			carry, val = divmod(sum, 10)

			mainPoint.next = ListNode(val)
			mainPoint = mainPoint.next

		return head.next

l1 = [1,2,3]
l2 = [4,5]
a = makeLinkedList(l1)

f = makeLinkedList(l2)

tail = Solution()
asa = tail.addTwoNumbers(a,f)

#asa = makeLinkedList(a)
while asa != None:
	print(f"{asa.val} ->", end= " ")
	asa = asa.next
